from celery import states
from celery.exceptions import Ignore
from app import celery, db
from app.models.video import Video
from app.utils.grpc_client import sync_lip
from moviepy.editor import VideoFileClip, AudioFileClip
import os

@celery.task(bind=True)
def process_video_task(self, audio_path, character_name, video_id):
    audio_clip = AudioFileClip(audio_path)
    audio_duration = audio_clip.duration
    
    video_path = os.path.join('video_material', f'{character_name}.mp4')
    video_clip = VideoFileClip(video_path).subclip(0, audio_duration)
    
    temp_video_path = os.path.join('temp', f'{character_name}_temp.mp4')
    video_clip.write_videofile(temp_video_path)
    
    # 修改這裡：只保存文件名，不包含完整路徑
    output_filename = f'{video_id}.mp4'
    save_path = os.path.join('app/static', output_filename)
    
    # 將相對路徑轉換為絕對路徑
    audio_path = os.path.abspath(audio_path)
    temp_video_path = os.path.abspath(os.path.join('temp', f'{character_name}_temp.mp4'))
    absolute_save_path = os.path.abspath(save_path)
    
    try:
        result = sync_lip(audio_path, temp_video_path, absolute_save_path)
        if result['status'] == 'success':
            video = Video.query.get(video_id)
            if video:
                video.video_url = f'/static/{output_filename}'
                db.session.commit()
            return {'status': '成功', 'video_id': video_id}
        else:
            raise Exception(result['message'])
    except Exception as e:
        self.update_state(state=states.FAILURE, meta={'exc_type': type(e).__name__, 'exc_message': str(e)})
        raise Ignore()  # 使用 Ignore() 來防止 Celery 重試任務
    finally:
        # 清理临时文件
        os.remove(audio_path)
        os.remove(temp_video_path)
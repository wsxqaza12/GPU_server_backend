from celery import states
from celery.exceptions import Ignore
from app import celery, db
from app.models.video import Video
from app.utils.grpc_client import sync_lip
from moviepy.editor import VideoFileClip, AudioFileClip
import os

@celery.task(bind=True)
def process_video_task(self, audio_path, character_name, video_id):
    os.makedirs('static', exist_ok=True)

    audio_clip = AudioFileClip(audio_path)
    audio_duration = audio_clip.duration
    
    video_path = os.path.join('video_material', f'{character_name}.mp4')
    video_clip = VideoFileClip(video_path).subclip(0, audio_duration)
    
    temp_video_path = os.path.join('temp', f'{character_name}_temp.mp4')
    video_clip.write_videofile(temp_video_path)
    
    save_path = os.path.join('static', f'{character_name}_output.mp4')
    
    # 將相對路徑轉換為絕對路徑
    audio_path = os.path.abspath(audio_path)
    temp_video_path = os.path.abspath(os.path.join('temp', f'{character_name}_temp.mp4'))
    save_path = os.path.abspath(os.path.join('static', f'{video_id}_output.mp4'))
    
    try:
        result = sync_lip(audio_path, temp_video_path, save_path)
        if result['status'] == 'success':
            video = Video.query.get(video_id)
            if video:
                video.video_url = save_path
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
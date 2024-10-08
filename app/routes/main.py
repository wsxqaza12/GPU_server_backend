from flask import Blueprint, request, jsonify, current_app, send_from_directory
from app.tasks.video_processing import process_video_task
from app.models.video import Video
from app import db, celery
import os

main = Blueprint('main', __name__)

@main.route('/process_video', methods=['POST'])
def process_video():
    audio_file = request.files['audio']
    character_name = request.form['character_name']

    os.makedirs('temp', exist_ok=True)
    audio_path = os.path.join('temp', audio_file.filename)
    audio_file.save(audio_path)
    
    with current_app.app_context():
        video = Video(character_name=character_name)
        db.session.add(video)
        db.session.commit()
        current_app.logger.info(f"已創建視頻記錄，ID: {video.video_id}")
    
    task = process_video_task.delay(audio_path, character_name, video.video_id)
    
    return jsonify({'task_id': task.id, 'video_id': video.video_id}), 202

@main.route('/get_video/<video_id>', methods=['GET'])
def get_video(video_id):
    with current_app.app_context():
        video = Video.query.get(video_id)
        if video:
            if video.video_url is None:
                full_video_url = None
            else:
                # base_url = 'http://216.234.102.170:10639'
                full_video_url = video.video_url
            
            return jsonify({
                'id': video.video_id,
                'character_name': video.character_name,
                'video_url': full_video_url
            })
        else:
            return jsonify({'error': '未找到視頻'}), 404

@main.route('/debug_static/<path:filename>')
def debug_static(filename):
    static_folder = current_app.static_folder
    file_path = os.path.join(static_folder, filename)
    if os.path.exists(file_path):
        return send_from_directory(static_folder, filename)
    else:
        return f"File not found: {file_path}", 404
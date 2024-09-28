from app import db
import uuid

class Video(db.Model):
    video_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    character_name = db.Column(db.String(50), nullable=False)
    video_url = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<Video {self.video_id}>"
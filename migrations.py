
from app import create_app, db
from app.models.video import Video

app = create_app()
app.app_context().push()

# 在這裡導入所有的模型
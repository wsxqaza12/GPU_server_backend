import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from celery import Celery
from config import Config

db = SQLAlchemy()
migrate = Migrate()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    celery.conf.update(app.config)

    # 設置日誌
    if not app.debug:
        file_handler = logging.FileHandler('app.log')
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    from app.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
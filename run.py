from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

from app.config import Config, TestConfig
from app.extensions import db
from app.routes.persona_routes import init_routes

load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)

    if test_config:
        app.config.from_object(test_config)
    else:
        app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    init_routes(app)

    db_path = os.getenv('FILENAME')
    if not test_config:
        with app.app_context():
            if not os.path.exists(db_path):
                db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5555, debug=True)

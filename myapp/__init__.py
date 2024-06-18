import os
from typing import Optional
from flask import Flask
from myapp.main.routes import blueprint as main_blueprint

def create_app(config_name: Optional[str] = None) -> Flask:
    app = Flask(__name__)

    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'production')

    if config_name == 'development':
        app.config.from_object('myapp.main.config.DevelopmentConfig')
    elif config_name == 'production':
        app.config.from_object('myapp.main.config.ProductionConfig')
    else:
        raise ValueError("Unknown configuration")

    app.register_blueprint(main_blueprint)

    return app

app: Flask = create_app()

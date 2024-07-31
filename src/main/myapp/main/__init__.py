from flask import Flask
from myapp.main.routes import blueprint as main_blueprint

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)
    app.register_blueprint(main_blueprint)
    return app

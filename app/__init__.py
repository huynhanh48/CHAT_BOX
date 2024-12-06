import os
import  dotenv
from flask  import Flask
from .config import app_config
def  create_app(config_name=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")

    from .Home import home_page as home_blueprint
    app.register_blueprint(home_blueprint)
    
    return  app
    
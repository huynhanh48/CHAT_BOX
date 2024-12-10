import os
import  dotenv
from flask  import Flask
from .config import app_config
from .db_conection import db,migrate,login_manager
from  .moduls import User,File_Session
def  create_app(config_name=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("config.py")

    db.init_app(app)
    migrate.init_app(app,db)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth_pages.login"
    
    from .Home import home_page as home_blueprint
    from .Auth import auth_pages as  auth_blueprint
    from .Uploads import  uploads_pages as uploads_blueprint
    app.register_blueprint(home_blueprint)
    app.register_blueprint(auth_blueprint,url_prefix='/auth')
    app.register_blueprint(uploads_blueprint)
    
    return  app

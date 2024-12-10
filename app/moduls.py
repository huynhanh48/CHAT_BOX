from  flask_login import UserMixin
from  .db_conection import  db,login_manager
from  werkzeug.security import generate_password_hash ,check_password_hash
from sqlalchemy import Column, Integer, DateTime,String,Boolean
import datetime
class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(60),unique=True,nullable=False)
    user_name = db.Column(db.String(60),unique=True,nullable=False)
    password_hash = db.Column(db.String(256),nullable=False)
    @property
    def password(self):
        raise AttributeError('password is not readable attribute')
    @password.setter
    def  password(self,password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self,password):
        return  check_password_hash(self.password_hash,password)
    def __repr__(self):
        return  self.user_name
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class File_Session(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(60),nullable=False)
    date_time = db.Column(DateTime,default=datetime.datetime.now)
    file_url = db.Column(String(256),nullable=False,unique=True)
    status = db.Column(Boolean(),default=False)
    
    def __repr__(self):
        return  self.file_url

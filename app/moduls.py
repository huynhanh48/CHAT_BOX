from  flask_login import UserMixin
from  .db_conection import  db,login_manager
from  werkzeug.security import generate_password_hash ,check_password_hash
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
        return  "<employment:{}>".format(self.user_name)
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
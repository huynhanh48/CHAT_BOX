from  flask_wtf import FlaskForm
from  wtforms import StringField,PasswordField,EmailField,SubmitField,ValidationError
from  wtforms.validators import  Length,DataRequired,Email,EqualTo
from ..moduls import User
class Register(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    user_name = StringField('name',validators=[DataRequired(),Length(max=20)])
    password = PasswordField('password',validators=[DataRequired(),EqualTo('confirm_password')])
    confirm_password=PasswordField('confirm_password')
    submit = SubmitField('register')

    # def validate_email(self,field):
    #     if(User.query.filter_by(email=field.data).first()):
    #         raise  ValidationError('email already')
        
    # def validate_username(self,field):
    #     if(User.query.filter_by(user_name=field.data).first()):
    #         raise ValidationError('user name already')
        
class Login(FlaskForm):
    email= StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    submit = SubmitField('login')
    
    # def validate_email(self,field):
    #     user =User.query.filter_by(email=field.data).first()
    #     if(not user):
    #         raise  ValidationError('email does not exist')
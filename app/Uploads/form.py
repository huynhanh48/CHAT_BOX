from  flask_wtf import  FlaskForm
from  flask_wtf.file import  FileAllowed
from  wtforms import  FileField,ValidationError,SubmitField
from  wtforms.validators import DataRequired

class Upload(FlaskForm):
    files = FileField('files', validators=[DataRequired(), FileAllowed(['csv'], 'CSV Only')])
    submit = SubmitField('Upload File')
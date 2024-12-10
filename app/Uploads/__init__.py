from flask import Blueprint, render_template, flash,redirect,url_for
from  flask_login import current_user,login_required
import os
from .form import Upload
from  ..moduls import  File_Session
from ..db_conection import db
from datetime import date
import datetime
import re

uploads_pages = Blueprint('uploads_pages', __name__)

@uploads_pages.route('/uploadfile', methods=['GET', 'POST'])
@login_required
def loadfile():
    form = Upload()
    form_file = File_Session.query.all()
    for i in range(len(form_file)):
        temp_link = re.split(r'\\',form_file[i].file_url)
        form_file[i].file_url= temp_link[-1]

    if form.validate_on_submit():
        print('Validation Passed')
        
        # Process the file upload
        file = form.files.data  # Access the uploaded file
        path = os.path.dirname(__file__)  # Current directory of this file
        path = os.path.dirname(path)  # Parent directory
        upload_folder = os.path.join(path, 'static', 'files')  # Final destination path for the file
        
        # Ensure the 'Uploads' directory exists
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        file_path = os.path.join(upload_folder, file.filename)
        current_date =datetime.datetime.now()
        file_databse = File_Session(date_time=current_date,author=current_user,file_url=file_path,status=False)
        if(not File_Session.query.filter_by(file_url=file_databse.file_url).first()):
            db.session.add(file_databse)
            db.session.commit()
            file.save(file_path)
            flash(f'File uploaded to: {file_databse.date_time}', 'success')
            return redirect(url_for('uploads_pages.loadfile'))
        if(File_Session.query.filter_by(file_url=file_databse.file_url).first()):
            flash('file already !','warring')
        
    return render_template('Uploads/loadfile.html', form=form ,form_file=form_file )

@uploads_pages.route('/remove/<int:id>',methods=['GET','POST'])
@login_required
def remove(id:int):
    file_session = File_Session.query.get(id)
    if not file_session:
        flash('File not found', 'danger')
        return redirect(url_for('uploads_pages.loadfile')) 
    db.session.delete(file_session)
    db.session.commit()
    if os.path.exists(file_session.file_url):
        os.remove(file_session.file_url)
    flash('Delete File CSV Success','success')
    return redirect(url_for('uploads_pages.loadfile'))
from flask import Blueprint, render_template, flash,redirect,url_for
import os
from .form import Upload
from  ..moduls import  File_Session
from datetime import date

uploads_pages = Blueprint('uploads_pages', __name__)

@uploads_pages.route('/uploadfile', methods=['GET', 'POST'])
def loadfile():
    form = Upload()
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
        # file_databse = File_Session(date_time=date.today(),)
        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)  # Save the file to the destination
        
        # Return success message or flash message
        flash(f'File uploaded to: {file_path}', 'success')
        return redirect(url_for('uploads_pages.loadfile'))

    return render_template('Uploads/loadfile.html', form=form)
from flask import Blueprint, flash, render_template, redirect, url_for
from .form import Register
from ..moduls import User
from ..db_conection import db

auth_pages = Blueprint('auth_pages', __name__)

@auth_pages.route("/register", methods=['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():
       
        if User.query.filter_by(email=form.email.data).first():
            flash('email already', 'danger')
            return render_template('Auth/register.html', form=form)

        
        if User.query.filter_by(user_name=form.user_name.data).first():
            flash('user name already', 'danger')
            return render_template('Auth/register.html', form=form)

        # Tạo mới người dùng
        employ = User(email=form.email.data, user_name=form.user_name.data, password=form.password.data)
        db.session.add(employ)
        db.session.commit()
        flash('register success', 'success')
        return redirect(url_for('auth_pages.login'))  # Redirect to login page
    return render_template('Auth/register.html', form=form)

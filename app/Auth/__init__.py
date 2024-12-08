from flask import Blueprint, flash, render_template, redirect, url_for
from .form import Register,Login
from ..moduls import User
from ..db_conection import db
from flask_login import login_user,logout_user,login_required

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

       
        employ = User(email=form.email.data, user_name=form.user_name.data, password=form.password.data)
        db.session.add(employ)
        db.session.commit()
        flash('register success', 'success')
        return redirect(url_for('auth_pages.login'))  
    return render_template('Auth/register.html', form=form)

# @auth_pages.route('/login',methods=['GET','POST'])
# def login():
#     form =Login()
#     if(form.validate_on_submit()):
#         user = User.query.filter_by(email=form.email.data).first()
#         print(user)
#         if(not user):
#             flash('invalid email','danger')
#             return  render_template('Auth/login.html',form = form)
#         elif (user.verify_password(form.password.data)):
#             flash('login success','success')
#             login_user(user)
#             return  redirect(url_for('home_page.home'))
#         else:
#             flash('please  check your login  and try again.','danger')
#             return  render_template('Auth/login.html',form = form)
#     return   render_template('Auth/login.html',form = form)
@auth_pages.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        print("Form is valid")  # Check if form is valid
        print("Email entered:", form.email.data)  # Print email entered in the form
        user = User.query.filter_by(email=form.email.data).first()
        print(user)  # This should print the user object if found, or None if not found
        
        if not user:
            flash('Invalid email', 'danger')
            return render_template('Auth/login.html', form=form)
        elif user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('home_page.home'))
        else:
            flash('Please check your login and try again.', 'danger')
            return render_template('Auth/login.html', form=form)
    else:
        print("Form is not valid")  # Form validation failed
        print(form.errors)  # Print any form validation errors

    return render_template('Auth/login.html', form=form)


@auth_pages.route('/logout')
def logout():
    logout_user()  
    return redirect(url_for('home_page.home'))
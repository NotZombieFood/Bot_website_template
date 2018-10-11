# coding=utf-8

from app import app, db
from flask import render_template, redirect, url_for, request, send_from_directory
from app.forms import LoginForm, RegisterForm
from app.texts import Texts
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    #form.payment.errors.append('the error message')
    if current_user.is_authenticated:
        return redirect(url_for('chat'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            form.password.errors.append('Auth_error')
        login_user(user)
        return redirect(url_for('chat'))
    return render_template('login.html', title=Texts.login, form=form, register_message = Texts.register_message, form_error_message = Texts.form_error_message)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('chat'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title=Texts.register, user_exists = Texts.user_exists , email_exists= Texts.email_exists,form=form, login_message = Texts.login_message, form_error_message = Texts.form_error_message)

@app.route('/')
@login_required
def chat():
    return render_template('index.html')

@app.route('/payments')
def payments():
    return ''

@app.route('/static/<path:path>')
def send_static_files(path):
    return send_from_directory('static', path)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
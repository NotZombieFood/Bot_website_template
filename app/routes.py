from app import app
from flask import render_template, redirect, url_for, request, send_from_directory
from forms import LoginForm, RegisterForm
from texts import Texts

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #checkCredentials(form.username.data, form.password.data)
        return redirect('/')
    return render_template('login.html', title=Texts.login, form=form, register_message = Texts.register_message, form_error_message = Texts.form_error_message)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #registerUser(form.username.data, form.email.data, form.password.data)
        return redirect('/')
    return render_template('register.html', title=Texts.register, form=form, login_message = Texts.login_message, form_error_message = Texts.form_error_message)

@app.route('/')
def chat():
    return 'Homepage'

@app.route('/payments')
def payments():
    return ''

@app.route('/static/<path:path>')
def send_static_files(path):
    return send_from_directory('static', path)

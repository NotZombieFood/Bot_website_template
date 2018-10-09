from config import Config
import os
from forms import LoginForm, RegisterForm
from texts import Texts
from flask import Flask, render_template, flash, redirect, url_for
#from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)

#db = SQLAlchemy(app)
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #checkCredentials(form.username.data, form.password.data)
        return redirect('/')
    return render_template('login.html', title=Texts.login, form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #registerUser(form.username.data, form.email.data, form.password.data)
        return redirect('/')
    return render_template('register.html', title=Texts.register, form=form)

@app.route('/')
def chat():
    return 'Homepage'

@app.route('/payments')
def payments():
    return ''

if __name__ == '__main__':
    app.run(debug=True)
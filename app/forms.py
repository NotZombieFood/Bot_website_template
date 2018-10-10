# coding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email
from app.texts import Texts

class LoginForm(FlaskForm):
    username = StringField(Texts.user, validators=[DataRequired()])
    password = PasswordField(Texts.password, validators=[DataRequired()])
    submit = SubmitField(Texts.login)

class RegisterForm(FlaskForm):
    username = StringField(Texts.user, validators=[DataRequired()])
    email = StringField(Texts.email, validators=[DataRequired(),Email()])
    password = PasswordField(Texts.password, validators=[DataRequired()])
    submit = SubmitField(Texts.register)

# coding=utf-8
import html

class Texts(object):
    login = html.escape('Iniciar sesión')
    password = html.escape('Contraseña')
    enter_password = html.escape('Ingresar contraseña')
    user = html.escape('Usuario')
    email = html.escape('Correo electrónico')
    register = html.escape('Registrarse')
    register_message = html.escape('¿No tienes cuenta? Regístrate.')
    login_message = html.escape('¿Tienes cuenta? Inicia sesión.')
    form_error_message = html.escape('Por favor rellena todos los campos.')
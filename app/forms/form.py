from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, ValidationError

class LoginForm(FlaskForm):
    """
    Formulário de login.
        - Nome de usuário
        - Senha
    """
    username = StringField('Username', validators=[
        DataRequired(message="Campo obrigatório."),
        Length(min=3, message="O nome de usuário deve ter no mínimo 4 caracteres.")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message="Campo obrigatório."),
        Length(min=8, message="A senha deve ter no mínimo 8 caracteres.")
    ])

class RegisterForm(FlaskForm):
    """
    Formulário de registro.
        - Nome
        - Nome de usuário
        - Email
        - Senha
    """
    name = StringField('Name', validators=[
        DataRequired(message="Campo obrigatório."),
        Length(min=3, message="O nome deve ter no mínimo 4 caracteres.")
    ])
    username = StringField('Username', validators=[
        DataRequired(message="Campo obrigatório."),
        Length(min=3, message="O nome de usuário deve ter no mínimo 4 caracteres.")
    ])
    email = EmailField('Email', validators=[
        DataRequired(message="Campo obrigatório.")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message="Campo obrigatório."),
        Length(min=8, message="A senha deve ter no mínimo 8 caracteres.")
    ])

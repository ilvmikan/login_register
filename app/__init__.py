from flask import Flask

app = Flask(__name__)

# Crie uma secret key para utilizar os formulários com CSRF
app.config['SECRET_KEY'] = ''

from app.controllers import index
from app.controllers import login
from app.controllers import register
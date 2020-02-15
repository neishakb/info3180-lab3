from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hi there!'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = '8ba060ec7dc24c'
app.config['MAIL_PASSWORD'] = '75b3ad54933c58'

mail = Mail(app)
app.config.from_object(__name__)

from app import views
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)


app.config['SECRET_KEY'] = '4d4dc0cd5e830f7356438e980dfeb96f'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail(app)

app.app_context().push()


from flask_blog.users.routes import users
from flask_blog.main.routes import main
from flask_blog.posts.routes import posts



app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(posts)

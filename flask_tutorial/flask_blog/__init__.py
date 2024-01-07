from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)


app.config['SECRET_KEY'] = '4d4dc0cd5e830f7356438e980dfeb96f'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.app_context().push()


from flask_blog import routes
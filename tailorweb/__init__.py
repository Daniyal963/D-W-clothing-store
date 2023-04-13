from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_admin import Admin



app = Flask(__name__)

app.config['SECRET_KEY'] = 'c96418b075871ec41adaea54fee6f4ac'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'email'
app.config['MAIL_PASSWORD'] = 'passowrd'
mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #function name of our route like url_for
login_manager.login_message_category = 'info' #bootstrap class




admin = Admin(app)


from tailorweb import routes

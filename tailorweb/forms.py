from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,SelectField,FieldList,FormField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from tailorweb.models import *

from flask_wtf import FlaskForm
from flask_wtf.File import FileAllowed,FileField
from wtforms import StringField, PasswordField,RadioField,TextAreaField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class ProfileForm(FlaskForm):
    image=FileField("Image", validators=[InputRequired()]) 
    fname = StringField('Firstname', validators=[InputRequired()]) 
    lname = StringField('Lastname', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    age = StringField('Age', validators=[InputRequired()])
    gender = RadioField('Gender',choices=[('Male','Male'),('Female','Female')])
    bio = TextAreaField('Biography', validators=[InputRequired()])
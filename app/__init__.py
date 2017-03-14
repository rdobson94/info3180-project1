from flask import Flask
from flask_sqlalchemy import SQLAlchemy


SECRET_KEY = 'Lets keep this a secret'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user123:password@localhost/user123"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning


db = SQLAlchemy(app)




app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = "app/static/uploads"


from app import views




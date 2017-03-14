from . import db
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey

class User(db.Model):
    __tablename__ = 'profiles'
    id=db.Column(db.Integer,primary_key=True,nullable=False,unique=True)
    userimage=db.Column(db.String(256))
    username=db.Column(db.String(256),unique=True)
    userfname=db.Column(db.String(256))
    userlname=db.Column(db.String(256))
    userage=db.Column(db.Integer)
    usergender=db.Column(db.String(120))
    userbio=db.Column(db.String(256))
    usertime=db.Column(db.DateTime,nullable=False)
    
    
    def __init__(self,userimage,username,userfname,userlname,userage,usergender,userbio,usertime):
        self.userimage = userimage
        self.username = username
        self.userfname = userfname
        self.userlname = userlname
        self.userage = userage
        self.usergender = usergender
        self.userbio=userbio
        self.usertime=usertime
        
        

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)        
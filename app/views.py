"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from datetime import *
import os
import time
from app.models import User
from flask import render_template, request, redirect, url_for,flash,session,jsonify
from werkzeug.utils import secure_filename
from app import db
from app.models import User
from app.models import  *

#from app. import User

#from app import db


###
# Routing for your application.
###
file_folder = "app/static/uploads"

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")
    
def allowed_file(filename):
    prof_extensions=set(['jpg', 'jpeg', 'gif','png'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in prof_extensions     

@app.route('/userForm',methods=['GET','POST'])
def userForm():
    """Render the website's Create Profile Page"""
    """If form criteria met, add and commit to the DB"""
    if request.method=='POST':
        username=request.form['username']
        userfname =request.form['fname']
        userlname=request.form['lname']
        userage=request.form['age']
        usergender=request.form['gender']
        userbio=request.form['bio']
        usertime=datetime.now()
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(file_folder, filename))
            userimage=filename = secure_filename(file.filename)
            #init_db()
            
            db.Model.metadata.reflect(db.engine)   
            user=User(userimage,username,userfname,userlname,userage,usergender,userbio,usertime)
            db.session.add(user)
            db.session.commit()


        return redirect(url_for('home'))

            
        
    return render_template('userForm.html')

@app.route('/userProfile/<userid>', methods=['POST', 'GET'])
def userProfile(userid):
    #return render_template('createProfile.html')
    user = User.query.filter_by(id=userid).first()
    image = '/static/uploads/' + user.userimage
    if request.method == 'POST' or ('Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json') and id!="":
        return jsonify(
            id=user.id,
            image=user.image,
            username=user.username,
            userfname=user.userfname,
            userlname=user.userlname,
            usergender=user.usergender,
            userage=user.userage,
            userbio=user.userbio,   
            usertime=user.usertime)
    else:
        user = {'id':user.id,
        'image':image,
        'username':user.username,
        'fname':user.userfname,
        'lname':user.userlname,
        'age':user.userage,
        'gender':user.usergender,
        'bio':user.userbio,
        'time':timeinfo(user.usertime)}
    return render_template('userProfile.html', user=user)  
    
##QUERY ALL USERS IN THE POSTGRES DATABASE, ADD TO A LIST AND RETURN JSON TOKENS ASSOCIATED WITH EACH
@app.route('/profileList', methods=["GET", "POST"])
def profileList():
  allUsers = db.session.query(User).all()
  if request.method == "POST" or ('Content-Type' in request.headers and request.headers['Content-Type'] == 'application/json'):
    plist=[]
    for user in allUsers:
      plist.append({'id':user.id,'username':user.username})    #RETURN ONLY USERNAME AND ID
    return jsonify(users=plist)
  else:
    return render_template('profileList.html', users=allUsers)      
    
    


#RETURN A FORMATTED TIME WHEN CALLED FOR PROFILE DISPLAY (VIEW)
def timeinfo(entry):
    day = time.strftime("%a")
    date = time.strftime("%d")
    if (date <10):
        date = date.lstrip('0')
    month = time.strftime("%b")
    year = time.strftime("%Y")
    return day + ", " + date + " " + month + " " + year    


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
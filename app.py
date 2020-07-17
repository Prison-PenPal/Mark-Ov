from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_mail import Mail
from werkzeug.utils import secure_filename
from flask_mail import Message

import sys
import json
app = Flask(__name__)




import flask
import io






app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'mohammad1.choudhury@gmail.com',
    MAIL_DEFAULT_SENDER = 'mohammad1.choudhury@gmail.com',
    MAIL_PASSWORD = 'xbmqliagmpxqwmnv',
))

@app.route("/")
def index():

    return render_template("test.html")
@app.route("/Read")
def Read():
    return render_template("Read_test.html")

@app.route("/About")
def About():
    return render_template("About.html")


@app.route("/Submit", methods = ['GET'])
def submit():
    return render_template("Submit.html")

@app.route("/external")
def cool():
    url = 'https:arxiv.org//pdf//2007.06563.pdf'
    return redirect(url, code=307)

@app.route("/externals")    
def cools():
    url = 'https://arxiv.org//pdf//2003.09871.pdf'
    return redirect(url, code=307)



@app.route("/Submits", methods = ['POST', 'GET'])
def Submit():
   
    
    
    
    
    if request.method == 'POST':  
        file = request.files['file']  
        file.save(file.filename)  
        

        
        filetype = file.filename.split('.')[-1]
       


        email = "wafster1337@gmail.com"
        extension = file.filename.split('.')[-1]
        msg = Message('hey',
                    sender="mohammad1.choudhury@gmail.com",
                    recipients=[email])
    
    

    return render_template("Test.html")



if __name__ == "__main__":
    app.run(debug=True)

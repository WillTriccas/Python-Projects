from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import email_sender
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:Jasper2009@localhost/height_collector'
db = SQLAlchemy(app)

class Data(db.Model):
    _tablename_ = "data"
    id= db.Column(db.Integer, primary_key =True)
    email_ = db.Column(db.String, unique =True)
    height_ = db.Column(db.Integer)
     
    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods = ['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        if db.session.query(Data).filter(Data.email_ == email).count() == 0 :
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height,1) # this queries and rounds the average height of all users height data
            total_users = db.session.query(Data.height_).count()  # this is the amount of users that have entered their height
            email_sender.send_email(email, height, average_height, total_users)
            return render_template("success.html")
    return render_template("index.html" , text = "This email address has already been entered, please try again")

if __name__ == '__main__':
    app.debug =True
    app.run()

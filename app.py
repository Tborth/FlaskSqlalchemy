from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/postgres'

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer , primary_key =True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date_created = db.Column(db.DateTime,default = datetime.now)
    

@app.before_first_request
def before():
    db.create_all()

@app.route('/<name>/<location>')
def index(name,location):
    users = Users(name = name,location=location)
    db.session.add(users)
    db.session.commit()
    return '<h1> Added New User</h1>'
    
    
    
if __name__ == "__main__":
    app.run()
"""
database section 
it will take a feild


"""
#imported packages
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4


#create database,db
db = SQLAlchemy()

#creating a function to get uuid
def getUuid():
    return uuid4.hex()

#creating database table containing user id , email and password

class User(db.Model):
    id = db.Column(db.String(32), primary_key=True, unique=True, default=getUuid)
    email = db.Column(db.String(345),nullable=False, unique=True)
    password = db.Column(db.Text)
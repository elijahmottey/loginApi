"""This is where all my configurations files goes to

Keyword arguments:
database
mail 
redis configuration

"""
from dotenv import load_dotenv
import os,redis



class ApplicationConfig:
    #getting secret key form env file
    
    SECRET_KEY=os.environ.get('SECRET_KEY')
    
    #configuring the database
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///user.db' 
    SQLALCHEMY_ECHO =True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #adding redis configuration
    SESSION_TYPE='redis'
    SESSION_PERMANENT= False
    SESSION_use_signer = True
    SESSSION_REDIS = redis.from_url("redis://127.0.0.1:6379")
    


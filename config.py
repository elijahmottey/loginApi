"""This is where all my configurations files goes to

Keyword arguments:
database
mail 
redis configuration

"""
from dotenv import load_dotenv
import os



class ApplicationConfig:
    #getting secret key form env file
    
    SECRET_KEY=os.environ.get('SECRET_KEY')
    
    #configuring the database
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:////user.db'
    SQLALCHEMY_ECHO =True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    


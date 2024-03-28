from flask import Flask,request,jsonify
from models import db, User
from config import ApplicationConfig

from werkzeug.security import generate_password_hash,check_password_hash
 


app=Flask(__name__)

# configuration
app.config.from_object(ApplicationConfig)

#initializing database


    
#create a register route
@app.route('/register', methods=['POST'])
def register():
    firstName = request.json['firstName']
    lastName = request.json['lastName']
    email = request.json['email']
    password = request.json['password']
    
    #checking if the user is already in the system if user exist return 409
    userExist = User.query.filter_by(email=email).first() is not None
    if userExist:
        return jsonify({
            "error":"uauthorized"
        }),409
        
    #hashing password 
    #hashPassword = generate_password_hash(password)
    newUser = User(firstName=firstName,lastName=lastName,email=email, password=generate_password_hash(password))
    
    #adding new user to db
    db.session.add(newUser)
    #saving new user
    db.session.commit()
    
    return jsonify({
        "status":"sucessfully added"
    }),201

db.init_app(app)
with app.app_context():
    db.create_all()
# run file

if __name__ == '__main__':
    app.run(debug=True)
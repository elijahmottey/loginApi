from flask import Flask,request,jsonify,session
from models import db, User
from config import ApplicationConfig
from flask_session import Session
from werkzeug.security import generate_password_hash,check_password_hash
 


app=Flask(__name__)

# configuration
app.config.from_object(ApplicationConfig)

serverSession= Session(app)

#initializing database
db.init_app(app)
with app.app_context():
    db.create_all()


    
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
    
    
    
# user login
@app.route('/userLogin', methods=['POST'])
def userLogin():
    email = request.json['email']
    password = request.json['password']
    
    user = User.query.filter_by(email=email).first()
    
    if not user or user is None:
        return jsonify({"status":"uauthorized",
                         "error":"email is not correct"}),401
    
    if not check_password_hash(user.password,password):
         return jsonify({"status":"uauthorized",
                         "error":"password is not correct"}),401
    
    session['user_id']=user.id
    
    return jsonify({"status":"user login sucessful"}),201


# run file

if __name__ == '__main__':
    app.run(debug=True)
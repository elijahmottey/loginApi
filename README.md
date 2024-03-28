# Login API using Flask

## Description
This is a simple login API built using Flask framework in Python. It provides endpoints for user authentication which can be integrated with a React frontend to facilitate user login functionality. Redis server is utilized to store user sessions upon successful login. Sqlite database is use to store data from the user. Bcrypt was also employed to decrypt the password text .


## Technologies Used
- Flask
- Flask-SQLAlchemy
- Bcrypt
- Flask-Session
- Redis
- Sqlite
- 

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/elijahmottey/loginApi
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up Redis server:
   - Install Redis server according to your operating system.
   - Start the Redis server.

## Usage
1. Run the Flask application:
   ```
   python app.py
   ```

2. The API will be accessible at `http://localhost:5000`.

3. Use the following endpoints for user authentication:
   - **POST** `/login`: User login. Requires email and password in the request body.
   - **POST** `/register`: User is register.Requires username, email, password,
   - **GET** `/@me`

## Integration with React Frontend
To integrate this API with a React frontend:
1. Create a login form component in React.
2. Use Axios or Fetch API to make requests to the login API endpoints.
3. Upon successful login, store the session token returned by the API in the client-side storage (e.g., local storage or cookies).
4. For protected routes, send the session token with requests to the backend for authentication.

## Contributors
- Elijah Mottey


## License
see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- mentor

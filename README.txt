
# Python JWT Authentication and Authorization with Flask

This is a simple Flask web application that demonstrates JWT (JSON Web Token) authentication and authorization. Users can register, log in, and access a protected route that lists all created users.

## Getting Started

Follow these steps to run the application on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (3.7+)
- `pip` package manager
- SQLite database (included by default)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/python-jwt.git
   cd python-jwt
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scriptsctivate
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Open the `config.py` file in the `app` directory and configure your secret key and database URI as needed.

   ```python
   app.config['SECRET_KEY'] = 'your-secret-key'
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
   ```

2. Ensure that the database tables are created before the first request. Open `app/__init__.py` and add the following code:

   ```python
   # Create database tables
   with app.app_context():
       db.create_all()
   ```

### Running the Application

1. Start the Flask development server:

   ```bash
   flask run
   ```

   Your app will be running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

2. Use an API testing tool like Postman or `curl` to interact with the following routes:

   - `/register`: Register a new user.
   - `/login`: Log in and obtain a JWT token.
   - `/users`: Access a protected route that lists all created users. Include the JWT token in the `Authorization` header.

### Example API Requests

- Register a user:
   ```bash
   curl -X POST http://127.0.0.1:5000/register         -H "Content-Type: application/json"         -d '{"full_name": "John Doe", "username": "john", "password": "password123"}'
   ```

- Log in and obtain a JWT token:
   ```bash
   curl -X POST http://127.0.0.1:5000/login         -H "Content-Type: application/json"         -d '{"username": "john", "password": "password123"}'
   ```

- Access the protected `/users` route (replace `YOUR_JWT_TOKEN` with the actual JWT token obtained during login):
   ```bash
   curl -X GET http://127.0.0.1:5000/users         -H "Authorization: Bearer YOUR_JWT_TOKEN"
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Flask-JWT-Extended: [https://flask-jwt-extended.readthedocs.io/](https://flask-jwt-extended.readthedocs.io/)

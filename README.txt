
# Python JWT Authentication and Authorization with Flask

This is a simple Flask web application that demonstrates JWT (JSON Web Token) authentication and authorization. Users can register, log in, and access a protected route that lists all created users.

## Getting Started

Follow these steps to set up and run the application on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (3.7+)
- `pip` package manager
- SQLite database (included by default)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/vishal1610kamal/Python_Jwt_Sqlite.git
   cd Python_Jwt_Sqlite
   ```

2. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scriptsctivate
   ```

3. **Install Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Application:**

   Open the `__init__.py` file in the `app` directory and configure your secret key and database URI as needed.

   ```python
   app.config['SECRET_KEY'] = 'your-secret-key'
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
   ```

5. **Create Database Tables:**

   Ensure that the database tables are created before the first request. Open `app/__init__.py` and add the following code:

   ```python
   # Create database tables
   with app.app_context():
       db.create_all()
   ```

### Running the Application with Flask

1. **Run the Application:**

   Start the Flask development server:

   ```bash
   flask run
   ```

   Your app will be running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

2. **Test the APIs:**

   You can use an API testing tool like Postman or `curl` to interact with the following routes:

   - `/register`: Register a new user.
   - `/login`: Log in and obtain a JWT token.
   - `/users`: Access a protected route that lists all created users. Include the JWT token in the `Authorization` header.

### Running the Application Directly from Python

1. **Activate the Virtual Environment (if used):**

   If you're using a virtual environment, activate it:

   ```bash
   source venv/bin/activate  # On Windows, use venv\Scriptsctivate
   ```

2. **Run the Application:**

   Run the Flask app using the `app.py` script:

   ```bash
   python app.py
   ```

   Your app will be running at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. **Test the APIs:**

   You can use an API testing tool like Postman or `curl` to interact with the following routes:

   - `/register`: Register a new user.
   - `/login`: Log in and obtain a JWT token.
   - `/users`: Access a protected route that lists all created users. Include the JWT token in the `Authorization` header.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Flask-JWT-Extended: [https://flask-jwt-extended.readthedocs.io/](https://flask-jwt-extended.readthedocs.io/)

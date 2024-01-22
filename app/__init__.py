from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Create the Flask application
app = Flask(__name__)

# Configuration settings (modify as needed)
app.config['SECRET_KEY'] = 'eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTcwNTMxNDQwMywiaWF0IjoxNzA1MzE0NDAzfQ.RABUY4W-hCdNMkVOKq8xAh0FYA5Z4Hogtzf9DQXH5jE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///python_jwt.db'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-JWT-Extended
jwt = JWTManager(app)

# Import your routes after initializing Flask-JWT-Extended
from app import routes

# Function to create database tables before the first request
with app.app_context():
    db.create_all()


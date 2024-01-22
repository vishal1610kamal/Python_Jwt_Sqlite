from app import app, db
from flask import request, jsonify
from app.models import User
from werkzeug.security import generate_password_hash
from app.auth import encode_auth_token
from flask_jwt_extended import jwt_required

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    # Check for existing user
    user = User.query.filter_by(username=data['username']).first()
    if user:
        return jsonify({'message': 'User already exists.'}), 409

    try:
        new_user = User(
            full_name=data['full_name'],
            username=data['username'],
            password_hash=generate_password_hash(data['password'])
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User successfully registered.'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    # Get data from request
    data = request.get_json()

    # Verify user
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        # Generate auth token
        auth_token = encode_auth_token(user.id)
        return jsonify({'auth_token': auth_token}), 200  # Updated line
    else:
        return jsonify({'message': 'Invalid username or password.'}), 401

# Protected route to list all users
@app.route('/users', methods=['GET'])
@jwt_required()  # Protect the route with JWT token authentication
def list_users():
    try:
        # Query the database for all users
        users = User.query.all()

        # Create a list of user data
        user_list = []
        for user in users:
            user_data = {
                'id': user.id,
                'full_name': user.full_name,
                'username': user.username,
            }
            user_list.append(user_data)

        return jsonify({'users': user_list}), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 500

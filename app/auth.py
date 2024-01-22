import jwt
import datetime
from flask import current_app

def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :param user_id: Identity of the user for whom the token is being generated
    :return: string (JWT token)
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),  # Token is valid for 1 day
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            current_app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return str(e)

def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token: JWT token to decode
    :return: integer|string (User ID or an error message)
    """
    try:
        payload = jwt.decode(auth_token, current_app.config.get('SECRET_KEY'), algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

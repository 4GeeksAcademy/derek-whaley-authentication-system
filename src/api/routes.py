"""
This module takes care of starting the API Server, loading the DB,
and adding the endpoints including authentication.
"""
from flask import request, jsonify, Blueprint
from flask_cors import CORS
from api.models import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api = Blueprint('api', __name__)
CORS(api)

@api.route('/hello', methods=['GET'])
def handle_hello():
    return jsonify({"message": "Hello from the backend!"}), 200

@api.route('/signup', methods=['POST'])
def signup():
    body = request.get_json()
    email = body.get("email")
    password = body.get("password")

    if not email or not password:
        return jsonify({"msg": "Email and password required"}), 400

    user_exists = User.query.filter_by(email=email).first()
    if user_exists:
        return jsonify({"msg": "User already exists"}), 400

    user = User(email=email, password=password, is_active=True)
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created successfully"}), 200

@api.route('/token', methods=['POST'])
def create_token():
    body = request.get_json()
    email = body.get("email")
    password = body.get("password")

    user = User.query.filter_by(email=email, password=password).first()
    if not user:
        return jsonify({"msg": "Invalid credentials"}), 401

    token = create_access_token(identity=user.id)
    return jsonify({"token": token}), 200

@api.route('/private', methods=['GET'])
@jwt_required()
def private():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if user is None:
        return jsonify({"msg": "User not found"}), 404

    return jsonify({"msg": f"Welcome, {user.email}!"}), 200




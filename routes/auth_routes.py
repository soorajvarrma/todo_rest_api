"""
Routes for authentication
"""
import os
from flask import Blueprint, request, jsonify
from services.auth_service import AuthService


auth_service = AuthService()

auth_bp = Blueprint('auth', __name__, url_prefix="/auth")

secret_key = os.getenv("SECRET_KEY")

@auth_bp.post('/register')
def register():
    """Registers the user

    Returns:
        message: success/failure
    """
    register_details = request.get_json()
    response = auth_service.register(request=register_details)
    if "error" in response:
        return jsonify(
            {"code": 400, "status": "failed", "message": response, "data": {}}
        )
    return jsonify(
        {
            "code": 201,
            "status": "success",
            "message": "User registered successfully",
            "data": response
        }
    )

@auth_bp.post('/login')
def login():
    """Checks if the login credentials are correct and logs the user in if so

    Returns:
        message: success/failure
    """
    data = request.get_json()
    response = auth_service.login(request=data,key=secret_key )
    if "error" in response:
        return jsonify(
            {"code": 400, "status": "failed", "message": response, "data": {}}
        )
    return jsonify(
        {
            "code": 201,
            "status": "success",
            "message": response,
            "data": {},
        }
    )

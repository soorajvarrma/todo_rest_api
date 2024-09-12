"""Contains the class that handles all the data handling for login
"""

import datetime
import jwt
from mongoengine import connect, NotUniqueError, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from core.model.User import User, UserSchema,UserLoginSchema
from flask import Response

connect("myDatabase")


class UserDataHandler:
    """Handles the data for login"""

    def __init__(self) -> None:
        self.data_handler = User()
        self.user_schema = UserSchema()
        self.login_schema = UserLoginSchema()
        self.users_schema = UserSchema(many=True)
        
    def login(self, login_details:dict, key:str) -> Response:
        """Checks if the username and password match and return JWT token if they do

        Args:
            login_details (json): Login credentials

        Returns:
            Response: Token
        """
        errors = self.login_schema.validate(login_details)
        if errors:
            return {"error": errors}
        username = login_details["username"]
        user = User.objects.filter(username=username).first()
        hashed_password = login_details["password"]
        if user and check_password_hash(user.password, hashed_password):
            token = jwt.encode(
                {
                    "identity": username,
                    "exp": datetime.datetime.now() + datetime.timedelta(hours=1),
                },
                key,
                algorithm="HS256",
            )
            return ({"token": token, "message": "Login successful"})
        return ({"error": "Invalid credentials"})

    def register(self, data:dict) -> Response:
        """Registers the user to the database

        Args:
            data (dict): username, email and password

        Returns:
            Response: success/failure
        """
        user = User(
            username=data["username"],
            email=data["email"],
            password=generate_password_hash(data["password"]),
        )
        errors = self.user_schema.validate(data)
        if errors:
            return {"error": errors}
        
        try:    
            user.save()
            current_user = User.objects.filter(username=data['username']).first()
            return self.user_schema.dump(current_user)
        
        except NotUniqueError as error:
            return {"error": str(error)}
        
        except ValidationError as error:
            return {"error": str(error)}
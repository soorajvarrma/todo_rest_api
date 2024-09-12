from flask import Response
from handlers.auth_handler import UserDataHandler

class AuthService():
    """Service layer of the login"""
    def __init__(self) -> None:
        self.handler = UserDataHandler()
        
    def register(self, request:dict)->Response:
        """Sends the details to the handler

        Args:
            request (json): sent by the user

        Returns:
            Response: message (success/failure)
        """
        response = self.handler.register(data=request)
        return response
    
    def login(self, request:dict, key:str)->Response:
        """Sends the details to the handler

        Args:
            request (json): sent by the user

        Returns:
            Response: message (success/failure)
        """
        response = self.handler.login(login_details=request,key=key)
        return response
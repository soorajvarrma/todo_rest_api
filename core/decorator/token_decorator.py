from functools import wraps

from flask import request, jsonify

def token_required(f):
    """Decorator

    Args:
        f (function): _description_

    Returns:
        _type_: _description_
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"message": "Token is missing!"}), 403

        return f(*args, **kwargs)

    return decorated


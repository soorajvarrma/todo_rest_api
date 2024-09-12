"""Main app file"""
import os
from flask import Flask
from routes.todo_routes import todo_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

app.register_blueprint(todo_bp)
app.register_blueprint(auth_bp)


if __name__ == "__main__":
    app.run(debug=True)

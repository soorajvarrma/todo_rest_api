"""Handles all the routes

Keyword arguments:
argument -- description
Return: return_description
"""

from flask import request, jsonify, Blueprint
from services.service import TodoRequestService
from core.decorator.token_decorator import token_required

todo_bp = Blueprint("todo_blueprint", __name__, url_prefix="/todo")

req = TodoRequestService()


@todo_bp.get("/posts")
def view():
    """Sends GET request to the get function of the class and returns the response

    Returns:
        response: list of all the tasks
    """
    request_args = request
    response = req.view_tasks(request=request_args)
    return {"code": 200, "status": "success", "message": "OK", "response": response}

@todo_bp.get("/search")
def search_by_text():
    """Sends a subtext of the task name to retreive all the tasks that contains that subtext

    Returns:
        response: list of all the tasks that match the criteria
    """
    request_args = request
    response = req.search_task_name(request=request_args)
    if response:
        return {"code": 200, "status": "success", "message": "OK", "data": response}
    return {"code": 400, "status": "failed", "message": "Not found", "data": {}}


@todo_bp.post("/add")
@token_required
def add():
    """Sends request to the post function of the class and returns the response

    Returns:
        response: Status code and a string
    """

    response = req.add_task(request=request)
    if "error" in response:
        return jsonify({"code": 400, "status": "failed", "error": response, "data": {}})

    return jsonify(
        {
            "code": 201,
            "status": "success",
            "message": "POSTED OK",
            "data": response,
        }
    )


@todo_bp.put("/done")
def edit():
    """updates a specific task as done"""
    arg = request.get_json()
    response = req.edit(request=arg)
    if response == 1:
        return {"code": 200, "status": "success", "message": "OK", "data": {}}
    return {"code": 400, "status": "failed", "message": "Not found", "data": {}}


@todo_bp.delete("/delete")
def remove():
    """Removes the task"""
    arg = request.get_json()
    response = req.delete(request=arg)
    return {"code": 200, "status": "success", "message": "OK", "data": response}


@todo_bp.get("/filter")
def filtered():
    """Filters the tasks by the parameter"""
    arg = request.get_json()
    response = req.filtered_by_task(request=arg)
    if response:
        return {"code": 200, "status": "success", "message": "OK", "data": response}
    return {"code": 400, "status": "failure", "message": "Not found", "data": {}}

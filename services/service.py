"""Handles all the routes
"""

from flask import Response
from handlers.todo_handler import TodoDataHandler
from core.model.tasks import Task


class TodoRequestService:
    """Handles all the requests sent by the views"""

    def __init__(self) -> None:
        self.handler = TodoDataHandler()

    def add_task(self, request) -> Response:
        """Posts a todo task

        Args:
            request: request

        Returns:
            Response: status code, string
        """
        task = request.get_json()
        response = self.handler.task_adder(task_req=task)
        return response

    def view_tasks(self, request: dict) -> Response:
        """Gets all of tasks in the todo list

        Keyword arguments:
        Return: All the tasks that are posted
        """
        request_pages = request.args
        response = self.handler.tasks_viewer(page_details=request_pages)
        return response

    def search_task_name(self, request:dict):
        """Gets all of tasks in the todo list that contains the subtext

        Keyword arguments: request
        Return: All the tasks that are posted
        """
        request = request.get_json()
        response = self.handler.search_task_by_name(request_task=request)
        return response

    def filtered_by_task(self, request: dict):
        """Gets all the tasks in the todo list that satisfies the condition

        Args:
         request (dict): request
        """
        task_string = request
        response = self.handler.filter_documents(Task, **task_string)
        return response

    def edit(self, request: dict) -> Response:
        """Gets the request and sends it to the handler

        Args:
            request (dict): request

        Returns:
            Response: Success/failure message
        """
        string = request["task"]
        response = self.handler.task_done(task=string)
        return response

    def delete(self, request: dict) -> Response:
        """Gets the task to be deleted and sends it to the handler

        Args:
            request (dict): The requested if

        Returns:
            Response: Success/failure message
        """
        task = request["task"]
        response = self.handler.deleter(task_name=task)
        return response

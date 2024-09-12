"""Handles all the data from the database

Keyword arguments:
argument -- description
Return: return_description
"""

import datetime
from mongoengine import connect, ValidationError
from flask import Response
from core.model.tasks import Task, TaskSchema


# client = MongoClient("localhost", 27017)
# db = client.myDatabase
# posts = db.todo_tasks

connect("myDatabase")


class TodoDataHandler:
    """Handles all the data from service

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self) -> None:
        self.todo = Task()
        self.task_schema = TaskSchema()

    def tasks_viewer(self, page_details: dict) -> Response:
        """Views all the tasks in the database

        Returns:
            Response: All the tasks
        """
        page = page_details.get("page", 1, type=int)
        per_page = page_details.get("per_page", 2, type=int)
        skip = (page - 1) * per_page

        total_items = Task.objects.count()
        total_pages = (total_items // per_page) + 1

        items = Task.objects.skip(skip).limit(per_page)

        tasks_dict = self.task_schema.dump(items, many=True)
        if page <= total_pages:
            return {
                "total pages": total_pages,
                "page number": page,
                "total items": total_items,
                "data": tasks_dict,
            }
        return {"message": "End of items"}
    
    def search_task_by_name(self, request_task):
        """Views all the tasks in the database that contains the specific subtext

        Returns:
            Response: tasks
        """
        task_name = request_task.get("task")
        tasks = Task.objects.filter(task__icontains=task_name)
        return self.task_schema.dump(tasks, many=True)

    def task_adder(self, task_req: str) -> Response:
        """Adds the task in the database

        Args:
            task (str): String that describes the task

        Returns:
            Response: success/failure message
        """
        task_name = task_req["task"]
        errors = self.task_schema.validate(task_req)
        if errors:
            return {"error": errors}

        task = Task(task=task_name, done=False, date=datetime.datetime.today())
        task.save()

        return self.task_schema.dump(task)

    def filter_documents(self, model, **kwargs):
        """
        Filters documents of the specified model based on provided keyword arguments.

        :param model: The MongoEngine model class to query.
        :param kwargs: The keyword arguments representing field-value pairs to filter on.
        :return: A queryset of the filtered documents.
        """
        response = model.objects.filter(**kwargs)
        return self.task_schema.dump(response, many=True)

    def task_done(self, task: str) -> Response:
        """Uses the task name to mark it as done

        Args:
            task (str): task name

        Returns:
            Response: success/failure
        """
        try:
            response = Task.objects(task=task).update(set__done=True)
            return response
        except ValidationError:
            return {"error": "Validation Error"}

    def deleter(self, task_name: str) -> Response:
        """Uses the id of the task to delete the task from the database

        Keyword arguments:
        task_name: the task
        Return: success/failure message
        """
        try:
            task_to_delete = Task.objects.filter(task=task_name)
            task_to_delete.delete()
            return "Deleted"
        except ValidationError:
            return {"error": "Validation Error"}

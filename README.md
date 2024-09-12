# Todo API Documentation

## Overview
This API allows users to manage their tasks by adding, viewing, removing, and marking tasks as complete. It also provides routes for user registration and login to authenticate users for task management.


## Authentication
The API requires users to authenticate using a token. The `Add Posts` route is protected, so the user needs to use the `Login` route and use the token to access it. New User can use the `Register` route to register their credentials

---

## User Routes

### 1. Register User
- **Endpoint**: `/auth/register`
- **Method**: `POST`
- **Description**: Registers a new user.
- **Request Body**:
  ```json
  {
    "username": "string",
    "email": "email@email.com",
    "password": "string"
  }
  ```
- **Response**:
  - *Success*
  ```json
  {
    "code": 201,
    "data": {
        "email": "string@mail.com",
        "id": "66e16cc9c33f298d52215ee0",
        "username": "test user7"
    },
    "message": "User registered successfully",
    "status": "success"
  }
  ```
  - *Failure*
  ```json
  {
    "code": 400,
    "data": {},
    "message": 
    {
        "error": "error message"
    },
    "status": "failed"
  }
  ```
### 2. Register User
- **Endpoint**: `/auth/login`
- **Method**: `POST`
- **Description**: Logs in a user and provides a jwt token
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  - *Success*
  ```json
  {
    "code": 201,
    "data": {},
    "message": {
        "message": "Login successful",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...."
    },
    "status": "success"
  }
  ```
  - *Failure*
  ```json
  {
    "code": 400,
    "data": {},
    "message": 
    {
        "error": "error message"
    },
    "status": "failed"
  }
  ```


## Task Routes

### 1. Add Task (Protected)
- **Endpoint**: `/todo/add`
- **Method**: `POST`
- **Description**: Adds a new task.
- **Headers**:
  - `Authorization: Bearer <token>`
- **Request Body**:
  ```json
  {
    "task": "string"
  }
  ```
- **Response**:
  - *Success*
  ```json
  {
    "code": 201,
    "data": {
        "date": "2024-09-12",
        "done": false,
        "id": "66e2632d5cbfc11834ddefbf",
        "task": "string"
    },
    "message": "POSTED OK",
    "status": "success"
  }
  ```
  - *Failure*
  ```json
  {
    "code": 400,
    "data": {},
    "error": {
        "error": "error message"
    },
    "status": "failed"
  }
  ```

### 2. View Task 
- **Endpoint**: `/todo/posts`
- **Method**: `GET`
- **Description**: Views task(s).
- **Query Parameters (optional)**:
  <!-- - task: Filter tasks by their name.
  - due_date: Filter tasks by specific due date (YYYY-MM-DD).
  - done: Filter tasks by completion status (true or false). -->
  - page: page number (default: 1)
  - per page: results per page (default: 2)
- **Response**:
  - *Success*
  ```json
  {
    "code": 200,
    "message": "OK",
    "response": {
        "data": [
            {
                "date": "2024-08-27",
                "done": false,
                "id": "1",
                "task": "Do homework"
            },
            {
                "date": "2024-08-29",
                "done": false,
                "id": "2",
                "task": "Go shopping"
            }
        ],
        "page number": 1,
        "total items": 11,
        "total pages": 6
    },
    "status": "success"
  }
  ```

### 3. Complete Task 
- **Endpoint**: `/todo/done`
- **Method**: `PUT`
- **Description**: Put task as completed
- **Request Body**:
  ```json
  {
    "task": "string"
  }
  ```
- **Response**:
  - *Success*
  ```json
  {
    "code": 200,
    "data": {},
    "message": "OK",
    "status": "success"
  }
  ```
  -*Failure*
  ```json
  {
    "code": 400, 
    "data": {},
    "message": "Not found", 
    "status": "failed", 
  }
  ```

### 4. Remove Task 
- **Endpoint**: `/todo/delete`
- **Method**: `DELETE`
- **Description**: Remove task
- **Request Body**:
  ```json
  {
    "task": "string"
  }
  ```
- **Response**:
  - *Success*
  ```json
  {
    "code": 200,
    "data": {},
    "message": "OK",
    "status": "success"
  }
  ```
  -*Failure*
  ```json
  {
    "code": 400, 
    "data": {},
    "message": "Not found", 
    "status": "failed", 
  }
  ```

### 4. Filter Tasks 
- **Endpoint**: `/todo/filter`
- **Method**: `GET`
- **Description**: View task(s) based on one or more criterias
- **Request Body**:
  ```json
  {
    "done": "False",
    "date": "2024-09-03"
  }
  ```
- **Response**:
  - *Success*
  ```json
  {
    "code": 200,
    "data": [
        {
            "date": "2024-09-03",
            "done": false,
            "id": "66d6ea351c33e89223c0dd43",
            "task": "Do your homework"
        }
    ],
    "message": "OK",
    "status": "success"
  }
  ```
  - *Failure*
  ```json
  {
    "code": 400, 
    "data": {},
    "message": "Not found", 
    "status": "failed", 
  }
  ```

### 5. Search Tasks 
- **Endpoint**: `/todo/search`
- **Method**: `GET`
- **Description**: View task(s) based on a subtext of their task name
- **Request Body**:
  ```json
  {
    "task": "Do"
  }
  ```
- **Response**:
  - *Success*
  ```json
  {
    "code": 200,
    "message": "OK",
    "response": [
        {
            "date": "2024-08-27",
            "done": false,
            "id": "1",
            "task": "Do homework423"
        },
        {
            "date": "2024-09-03",
            "done": false,
            "id": "66d6ea351c33e89223c0dd43",
            "task": "Do your homework"
        }
    ],
    "status": "success"
  }
  ```
  - *Failure*
  ```json
  {
    "code": 400, 
    "data": {},
    "message": "Not found", 
    "status": "failed", 
  }
  ```
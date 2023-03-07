# API Endpoints:
## 1. Tasks

1. GET /api/tasks/
    - Returns a list of all tasks of the current user

2. POST /api/tasks/
    - Creates a new task
    - Request Body:
        - `title` (required): Task title
        - `description` (optional): Task description
        - `section` (optional): Task section ID
        - `status` (optional): Task status ID, default `todo`
        - `priority` (required): Task priority
        - `start_datetime` (required): Start datetime in ISO format (yyyy-MM-dd'T'HH:mm:ss.SSSXXX)
        - `due_datetime` (optional): Due datetime in ISO format (yyyy-MM-dd'T'HH:mm:ss.SSSXXX)

3. GET /api/tasks/<task_id>/
    - Returns details of a specific task
    - URL Parameters:
        - `task_id` (required): ID of the task

4. PUT /api/tasks/<task_id>/
    - Updates an existing task
    - URL Parameters:
        - `task_id` (required)
    - Request Body:
        - `title` (required): Task title
        - `description` (optional): Task description
        - `section` (optional): Task section ID
        - `status` (optional): Task status ID, default `todo`
        - `priority` (optional): Task priority
        - `start_datetime` (required): Start datetime in ISO format (yyyy-MM-dd'T'HH:mm:ss.SSSXXX)
        - `due_datetime` (optional): Due datetime in ISO format (yyyy-MM-dd'T'HH:mm:ss.SSSXXX)
5. PATCH /api/tasks/<task_id>/
    - Updates an existing task
    - URL Parameters:
        - `task_id` (optional)
    - Request Body:
        - `title` (optional): Task title
        - `description` (optional): Task description
        - `section` (optional): Task section ID
        - `status` (optional): Task status ID, default `todo`
        - `priority` (optional): Task priority
        - `start_datetime` (optional): Start datetime in ISO format (yyyy-MM-dd'T'HH:mm:ss.SSSXXX)
        - `due_datetime` (optional): Due datetime in ISO format (yyyy-MM-dd'T'HH:mm:ss.SSSXXX)

6. DELETE /api/tasks/<task_id>/
    - Deletes a specific task
    - URL Parameters:
        - `task_id` (required): ID of the task


## 2. Task sections

1. GET /api/sections/
    - Returns a list of all task sections of the current user

2. POST /api/sections/
    - Creates a new task section
    - Request Body:
        - `title` (required): Task section name
        - `color` (optional): Task section color in HEX format

3. GET /api/sections/<section_id>/
    - Returns details of a specific task section
    - URL Parameters:
        - `section_id` (required): ID of the task section

4. PUT /api/sections/<section_id>/
    - Updates an existing task section
    - URL Parameters:
        - `section_id` (required): ID of the task section
    - Request Body:
        - `title` (required): Task section name
        - `color` (optional): Task section color in HEX format

5. PATCH /api/sections/<section_id>/
    - Updates an existing task section
    - URL Parameters:
        - `section_id` (required): ID of the task section
    - Request Body:
        - `title` (optional): Task section name
        - `color` (optional): Task section color in HEX format

6. DELETE /api/sections/<section_id>/
    - Deletes a specific task section
    - URL Parameters:
        - `section_id` (required): ID of the task section


## 3. Task status

1. GET /api/statuses/
    - Returns a list of all task statuses of the current user

2. POST /api/statuses/
    - Creates a new task status
    - Request Body:
        - `title` (required): Task status name

3. GET /api/statuses/<status_id>/
    - Returns details of a specific task status
    - URL Parameters:
        - `status_id` (required): ID of the task status

4. PUT /api/statuses/<status_id>/
    - Updates an existing task status
    - URL Parameters:
        - `status_id` (required): ID of the task status
    - Request Body:
        - `title` (required): Task status name

5. PATCH /api/statuses/<status_id>/
    - Updates an existing task status
    - URL Parameters:
        - `status_id` (required): ID of the task status
    - Request Body:
        - `title` (optional): Task status name

6. DELETE /api/statuses/<status_id>/
    - Deletes a specific task status
    - URL Parameters:
        - `status_id` (required): ID of the task status


## 4. Users

1. POST /users/register/
   - Register user
   - Request Body:
     - `email` (required): user email address
     - `password` (required): user password 
     - `password2` (required): password that must match with password
     - `username` (required): username

## 5. authorization

1. POST /auth/token/
    - get access and refresh token
    - Request Body:
      - username (required)
      - password (required)
  
2. POST /auth/token/refresh/
    - Request Body:
      - refresh (required)
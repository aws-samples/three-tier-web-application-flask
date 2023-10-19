# API Documentation

## Introduction

Brief introduction to the Application Layer.


## Endpoints

### `GET /`

Get a list of todo tasks.

#### Parameters

- None

#### Response

```json
[
  {
    "id": "task-1"
  },
  {
    "1": "Get Milk"
  }
]
```
### `GET /health`

Get status code 200 with a message.

#### Parameters

- None

#### Response

```json
{
  "status_code": 200,
  "message": "Successful health check for ALB!"
}
```

### `POST /create`

Create a new todo task.

#### Headers
- Content-Type: `application/x-www-form-urlencoded`

#### Request Body
The request body should be URL-encoded and contain the following form parameters:

- **task** (string, required): The name of the todo task.

#### Response

```json
{
    "message": "Form submitted successfully!"
}

{
    "error": "Invalid form data. Please provide valid values for name, email, and message."
}
```

### `POST /update`

Update an existing todo task.

#### Headers
- Content-Type: `application/x-www-form-urlencoded`

#### Request Body
The request body should be URL-encoded and contain the following form parameters:

- **task_id** (string, required): The id of the todo task to update.
- **task** (string, required): The new name of the todo task.

#### Response

```json
{
    "message": "Form submitted successfully!"
}

{
    "error": "Invalid form data. Please provide valid values for name, email, and message."
}
```

### `POST /complete/<task_id>`

Complete an existing todo task.

- **task_id** (integer, required):  The id of the todo task to complete.

### Response

#### Status Codes
- 302 OK: User information retrieved successfully.
- 404 Not Found: User not found.

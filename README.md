# Notes API

A RESTful API for creating, reading, updating, and deleting notes, built with FastAPI and SQLAlchemy. Includes JWT authentication, automatic request validation, and persistent storage.

## Tech Stack

- **Python 3.12**
- **FastAPI** — web framework
- **Uvicorn** — ASGI server
- **SQLAlchemy** — ORM for database interaction
- **Pydantic** — data validation
- **SQLite** — database (local development)
- **PyJWT** and **bcrypt** — token handling and password hashing

## Features

- Full CRUD support for notes
- User registration and login with JWT authentication
- Protected note endpoints (valid token required)
- Request validation (e.g. rejects empty titles/content)
- Persistent storage — data survives server restarts
- Auto-generated interactive API documentation (Swagger UI)
- Proper REST status codes (201 on create, 204 on delete, 401 on missing or invalid token, 404 on missing resources, 409 on duplicate username, 422 on invalid input)

## Endpoints

The `/notes` endpoints require an `Authorization: Bearer <token>` header. Get a token from `/login`.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| POST | `/register` | Register a new user |
| POST | `/login` | Log in and receive a JWT |
| POST | `/notes` | Create a new note |
| GET | `/notes` | List all notes |
| GET | `/notes/{id}` | Get a single note by ID |
| PUT | `/notes/{id}` | Update an existing note |
| DELETE | `/notes/{id}` | Delete a note |

## Running Locally

(keep your existing steps 1–5 exactly as they are)

## Project Structure

```
notes-api/
├── app/
│   ├── __init__.py
│   ├── main.py       # API routes
│   ├── auth.py       # password hashing, JWT, get_current_user
│   ├── models.py     # SQLAlchemy database models
│   └── database.py   # Database connection setup
├── requirements.txt
├── .gitignore
└── README.md
```

## Status

Core CRUD and authentication are complete (registration, login, JWT-protected note endpoints). In progress: per-user note ownership, Docker support, and background task processing.
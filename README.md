# notes-api
# Notes API

A RESTful API for creating, reading, updating, and deleting notes, built with FastAPI and SQLAlchemy. Includes automatic request validation and persistent storage.

## Tech Stack

- **Python 3.12**
- **FastAPI** — web framework
- **Uvicorn** — ASGI server
- **SQLAlchemy** — ORM for database interaction
- **Pydantic** — data validation
- **SQLite** — database (local development)

## Features

- Full CRUD support for notes
- Request validation (e.g. rejects empty titles/content)
- Persistent storage — data survives server restarts
- Auto-generated interactive API documentation (Swagger UI)
- Proper REST status codes (201 on create, 204 on delete, 404 on missing resources, 422 on invalid input)

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| POST | `/notes` | Create a new note |
| GET | `/notes` | List all notes |
| GET | `/notes/{id}` | Get a single note by ID |
| PUT | `/notes/{id}` | Update an existing note |
| DELETE | `/notes/{id}` | Delete a note |

## Running Locally

1. Clone the repository:
```bash
   git clone git@github.com:harishprasad7698/notes-api.git
   cd notes-api
```

2. Create and activate a virtual environment:
```bash
   python -m venv venv
   venv\Scripts\Activate.ps1   # Windows PowerShell
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Run the server:
```bash
   uvicorn app.main:app --reload
```

5. Open the interactive docs:
http://127.0.0.1:8000/docs

## Project Structure    
notes-api/
├── app/
│ ├── init.py
│ ├── main.py # API routes
│ ├── models.py # SQLAlchemy database models
│ └── database.py # Database connection setup
├── requirements.txt
├── .gitignore
└── README.md

## Status

Core CRUD functionality complete. In progress: authentication (JWT), Docker support, and background task processing.    
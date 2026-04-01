# Candidate Management API

A REST API built with **FastAPI** and **SQLite** to manage candidates in a recruitment pipeline. Recruiters can add candidates, view them, filter by status, and update their application status through the hiring process.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.13 |
| Framework | FastAPI |
| Database | SQLite (via SQLAlchemy ORM) |
| Validation | Pydantic v2 |
| Server | Uvicorn |
| Testing | Pytest |

---

## Project Structure

```
Candidate_Management_API/
├── app/
│   ├── __init__.py             # Makes app a Python package
│   ├── main.py                 # App entry point, startup, router registration
│   ├── database.py             # DB engine, session factory, Base class
│   ├── db_models.py            # SQLAlchemy ORM model (Candidate table)
│   ├── schemas.py              # Pydantic schemas for request/response validation
│   └── routers/
│       ├── __init__.py
│       └── candidates.py       # All 3 API endpoints
├── tests/
│   └── test_candidates.py      # Pytest test cases
├── .env                        # Environment variables (not pushed to git)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/candidates` | Create a new candidate |
| `GET` | `/candidates` | Get all candidates (optional status filter) |
| `PUT` | `/candidates/{id}/status` | Update a candidate's status |
| `GET` | `/health` | Health check |

### Candidate Status Flow

```
applied  →  interview  →  selected
                      ↘  rejected
```

Valid status values: `applied`, `interview`, `selected`, `rejected`

---

## Prerequisites

- **Python 3.10+** — [Download here](https://www.python.org/downloads/)
- **pip** — comes bundled with Python
- **Git** — [Download here](https://git-scm.com/)

> SQLite does **not** need to be installed separately — it is built into Python.

---

## Setup & Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/candidate-management-api.git
cd candidate-management-api
```

### 2. Create a Virtual Environment
```bash
python -m venv myenv

# Windows
myenv\Scripts\activate

# Mac/Linux
source myenv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create Environment File
Create a `.env` file in the root folder:
```
DATABASE_URL=sqlite:///./candidates.db
```

### 5. Run the Server
```bash
uvicorn app.main:app --reload
```

### 6. Open API Docs
```
http://localhost:8000/docs
```

---

## Testing

### Swagger UI
Visit `http://localhost:8000/docs` — interactive forms for all endpoints, no extra tools needed.

### Postman
| Action | Method | URL | Body |
|---|---|---|---|
| Create candidate | POST | `/candidates` | `{"name":"John","email":"john@example.com","skill":"Python","status":"applied"}` |
| Get all | GET | `/candidates` | — |
| Filter by status | GET | `/candidates?status=applied` | — |
| Update status | PUT | `/candidates/1/status` | `{"status":"interview"}` |

### Pytest
```bash
python -m pytest tests/ -v
```

---

## Error Responses

| Scenario | Status Code |
|---|---|
| Duplicate email | `409 Conflict` |
| Candidate not found | `404 Not Found` |
| Invalid email / status | `422 Unprocessable Entity` |
| Server error | `500 Internal Server Error` |

---

## .gitignore

```
.env
myenv/
candidates.db
__pycache__/
.pytest_cache/
*.pyc
```
# Candidate Management API

A REST API built with **FastAPI** and **SQLite** to manage candidates in a recruitment pipeline. Recruiters can add candidates, view them, filter by status, and update their status through the hiring process.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Framework | FastAPI |
| Database | SQLite (via SQLAlchemy ORM) |
| Validation | Pydantic v2 |
| Server | Uvicorn |

---

## Project Structure

```
Candidate_Management_API/
├── app/
│   ├── __init__.py         # Makes app a Python package
│   ├── main.py             # App entry point, startup, router registration
│   ├── database.py         # DB engine, session, Base class
│   ├── db_models.py        # SQLAlchemy ORM model (Candidate table)
│   ├── schemas.py          # Pydantic schemas for request/response validation
│   └── routers/
│       ├── __init__.py
│       └── candidates.py   # All 3 API endpoints
├── tests/
│   └── test_candidates.py  # Pytest test cases
├── .env                    # Environment variables (not pushed to git)
├── .env.example            # Template for environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/candidates` | Create a new candidate |
| `GET` | `/candidates` | Get all candidates (filter by status) |
| `PUT` | `/candidates/{id}/status` | Update a candidate's status |
| `GET` | `/health` | Health check |

### Candidate Status Flow

```
applied  →  interview  →  selected
                      →  rejected
```

Valid status values: `applied`, `interview`, `selected`, `rejected`

---

## Prerequisites

Before running this project, make sure you have:

- **Python 3.10 or higher** — [Download here](https://www.python.org/downloads/)
- **pip** — comes bundled with Python
- **Git** — [Download here](https://git-scm.com/)

> SQLite does **not** need to be installed separately — it is built into Python.

---

## Run Locally (Your Own Machine)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/candidate-management-api.git
cd candidate-management-api
```

### 2. Create a Virtual Environment

```bash
# Create
python -m venv myenv

# Activate — Mac/Linux
source myenv/bin/activate

# Activate — Windows
myenv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
# Mac/Linux
cp .env.example .env

# Windows
copy .env.example .env
```

The default `.env` works out of the box — no changes needed for local SQLite setup.

### 5. Run the Server

```bash
uvicorn app.main:app --reload
```

### 6. Open API Docs

```
http://localhost:8000/docs
```

The SQLite database file `candidates.db` is created **automatically** in the project root when the server starts for the first time.

---

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `DATABASE_URL` | `sqlite:///./candidates.db` | Database connection string |

---

## Testing the API

### Option 1 — Swagger UI (Recommended)
Visit `http://localhost:8000/docs` — all endpoints are listed with interactive forms.

### Option 2 — Postman or curl

**Create a candidate:**
```bash
curl -X POST http://localhost:8000/candidates \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com", "skill": "Python", "status": "applied"}'
```

**Get all candidates:**
```bash
curl http://localhost:8000/candidates
```

**Filter by status:**
```bash
curl http://localhost:8000/candidates?status=interview
```

**Update status:**
```bash
curl -X PUT http://localhost:8000/candidates/1/status \
  -H "Content-Type: application/json" \
  -d '{"status": "interview"}'
```

---

## Run Tests

```bash
pytest tests/
```

---

## What Gets Created Automatically

| File | When | Purpose |
|---|---|---|
| `candidates.db` | On first server start | SQLite database file |
| Table `candidates` | On first server start | Created by `create_all()` in `main.py` |

> In production, table creation would be handled by Alembic migrations instead of `create_all()`.

---

## .gitignore — What is NOT in the Repo

```
candidates.db     ← database file (created locally)
.env              ← your secrets (use .env.example as template)
__pycache__/
myenv/
*.pyc
```
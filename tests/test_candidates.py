from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_candidate():
    res = client.post("/candidates/", json={
        "name": "Jane Doe", "email": "jane@test.com",
        "skill": "Python", "status": "applied"
    })
    assert res.status_code == 201
    assert res.json()["email"] == "jane@test.com"

def test_duplicate_email():
    client.post("/candidates/", json={
        "name": "Jane Doe", "email": "dup@test.com",
        "skill": "Go", "status": "applied"
    })
    res = client.post("/candidates/", json={
        "name": "Jane Again", "email": "dup@test.com",
        "skill": "Go", "status": "applied"
    })
    assert res.status_code == 409

def test_filter_by_status():
    res = client.get("/candidates/?status=applied")
    assert res.status_code == 200

def test_update_status():
    create = client.post("/candidates/", json={
        "name": "Bob", "email": "bob@test.com",
        "skill": "Java", "status": "applied"
    })
    cid = create.json()["id"]
    res = client.put(f"/candidates/{cid}/status", json={"status": "interview"})
    assert res.status_code == 200
    assert res.json()["status"] == "interview"
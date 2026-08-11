import os
import requests

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL") or "https://craft-nexus-14.preview.emergentagent.com"


def test_root_ready():
    response = requests.get(f"{BASE_URL}/api/", timeout=15)
    assert response.status_code == 200
    assert response.json()["message"] == "Cozy Loop Crochet is ready"


def test_contact_validation():
    response = requests.post(f"{BASE_URL}/api/contact", json={"name": "A", "email": "bad", "subject": "", "message": "short"}, timeout=15)
    assert response.status_code == 422
    assert "detail" in response.json()


def test_contact_persists_message():
    payload = {"name": "TEST Reviewer", "email": "test-reviewer@example.com", "subject": "TEST coverage", "message": "This is a regression test message."}
    response = requests.post(f"{BASE_URL}/api/contact", json=payload, timeout=15)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Thanks for reaching out! We'll be in touch soon."
    assert isinstance(data["id"], str) and data["id"]
from fastapi.testclient import TestClient

from app import app


def test_get_root():
    client = TestClient(app)
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

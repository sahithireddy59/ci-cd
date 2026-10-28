
from fastapi.testclient import TestClient
from app import main

client = TestClient(main.app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_analyze(monkeypatch):
    # Mock the AI response so tests run quickly
    def fake_analysis(logs):
        return {
            "analysis": "Database connection timeout",
            "resolution": "Check connection pool settings"
        }

    monkeypatch.setattr(
        main,
        "run_analysis",
        fake_analysis
    )

    response = client.post(
        "/analyze",
        json={
            "logs": "ERROR Database connection timeout"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["analysis"] == "Database connection timeout"
    assert data["resolution"] == "Check connection pool settings"


def test_empty_logs():
    response = client.post(
        "/analyze",
        json={"logs": ""}
    )

    assert response.status_code == 422

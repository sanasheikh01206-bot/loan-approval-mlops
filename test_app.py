import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_root_endpoint(client):
    """Test that the home page renders correctly."""
    response = client.get("/")
    assert response.status_code == 200


def test_prediction_post(client):
    """Test the prediction endpoint with a JSON payload."""
    payload = {
        "Gender": "Male",
        "Married": "Married",
        "Credit_History": "Clear Debts",
        "ApplicantIncome": 10000,
        "LoanAmount": 100,
    }
    response = client.post("/prediction", json=payload)
    assert response.status_code == 200
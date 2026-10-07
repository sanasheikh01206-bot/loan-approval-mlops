import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_root(client):
    """Verifies that the home endpoint is live."""
    resp = client.get("/")
    assert resp.status_code == 200


def test_predict_post(client):
    """Verifies the JSON POST endpoint (used by Newman/Postman)."""
    test_data = {
        "Gender": "Male",
        "Married": "Unmarried",
        "Credit_History": "Unclear Debts",
        "ApplicantIncome": 100000,
        "LoanAmount": 2000000,
    }
    resp = client.post("/prediction", json=test_data)
    assert resp.status_code == 200
    assert resp.json == {"loan_approval_status": "Rejected"}


def test_predict_get_browser(client):
    """Verifies the browser URL parameter GET request."""
    url = "/prediction?Gender=Male&Married=Unmarried&Credit_History=Unclear%20Debts&ApplicantIncome=100000&LoanAmount=2000000"
    resp = client.get(url)
    assert resp.status_code == 200
    assert resp.json == {"loan_approval_status": "Rejected"}
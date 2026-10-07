# 🏦 End-to-End Loan Approval Prediction Service (MLOps)

An end-to-end Machine Learning web application and API that predicts loan application approval status based on applicant demographics, financial profile, and credit history.

Containerized with Docker, continuously tested and built via GitHub Actions CI/CD, and published to Docker Hub.

---

## 📌 Project Overview

* **Objective:** Automate loan eligibility screening with real-time model inference.
* **Architecture:** Flask web server exposing both an interactive HTML form UI and programmatic JSON API endpoints.
* **Testing & CI/CD:** Automated test suite via `pytest` integrated into GitHub Actions, triggering automated Docker image builds and pushes to Docker Hub upon updates to the `main` branch.

---

## ⚡ Quickstart: Run with Docker (No Local Python Setup Needed)

You can pull and run the pre-built container directly on your machine using Docker:

docker pull sana01206/loan-approval-mlops:latest

### 2. Run the Container

```bash
docker run -d -p 5000:5000 --name loan-app sana01206/loan-approval-mlops:latest


### 3. Access the Application

* **Interactive UI:** Open your browser and navigate to:
`http://localhost:5000/`
* **Direct Prediction Endpoint:**
`http://localhost:5000/prediction`

---

## 📝 Input Features & Guidelines

| Feature | Description | Accepted Values / Format |
| --- | --- | --- |
| **Gender** | Applicant gender | `Male`, `Female` |
| **Married** | Applicant marital status | `Married`, `Unmarried` |
| **Credit_History** | Prior credit standing | `Clear Debts`, `Unclear Debts` |
| **ApplicantIncome** | Gross applicant income | Numerical (e.g., `5000` or `10000`) |
| **LoanAmount** | Requested loan amount (**in thousands**) | Numerical (e.g., `100` = $100,000) |

> ⚠️ **Important Note on Loan Amount:**
> The model expects `LoanAmount` expressed **in thousands**.
> For example:
> * Enter **`100`** to represent **$100,000 / ₹100,000**
> * Enter **`50`** to represent **$50,000 / ₹50,000**
> *(Entering `100000` directly will be interpreted by the model as 100 million, leading to high rejection rates).*
> 
> 

---

## 🔌 API Reference

### 1. Browser GET Request (Query Parameters)

```text
GET /prediction?Gender=Male&Married=Married&Credit_History=Clear Debts&ApplicantIncome=10000&LoanAmount=100

```

### 2. Programmatic POST Request (JSON Payload)

**Endpoint:** `POST http://localhost:5000/prediction`

**Headers:** `Content-Type: application/json`

**Request Body:**

```json
{
  "Gender": "Male",
  "Married": "Married",
  "Credit_History": "Clear Debts",
  "ApplicantIncome": 10000,
  "LoanAmount": 100
}

```

**Response:**

```json
{
  "Loan_Approval_Status": "Approved"
}

```

---

## 🛠️ Local Development & Testing

If you prefer running the source code locally without Docker:

1. **Clone the repository:**
```bash
git clone [https://github.com/sanasheikh01206-bot/loan-approval-mlops.git](https://github.com/sanasheikh01206-bot/loan-approval-mlops.git)
cd loan-approval-mlops

```


2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate          # On Windows

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Run the automated unit tests:**
```bash
pytest

```


5. **Start the local Flask server:**
```bash
python app.py

```



---

## 🚀 CI/CD Pipeline Summary

* **Testing:** Every commit or pull request triggers automated endpoint validation with `pytest`.
* **Container Registry:** Merges to `main` authenticate via Docker Hub tokens, build a multi-platform Docker image, and push to `sana01206/loan-approval-mlops:latest`.
* **Zero-Downtime Deployment Ready:** The generated Docker image can be deployed directly to cloud container environments like Render, AWS ECS, or GCP Cloud Run.

```

```

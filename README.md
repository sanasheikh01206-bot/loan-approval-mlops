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

### 1. Pull the Image from Docker Hub
```bash
docker pull sana01206/loan-approval-mlops:latest
2. Run the ContainerBashdocker run -d -p 5000:5000 --name loan-app sana01206/loan-approval-mlops:latest
3. Access the ApplicationInteractive UI: Open your browser and navigate to:http://localhost:5000/Direct Prediction Endpoint:http://localhost:5000/prediction📝 Input Features & GuidelinesFeatureDescriptionAccepted Values / FormatGenderApplicant genderMale, FemaleMarriedApplicant marital statusMarried, UnmarriedCredit_HistoryPrior credit standingClear Debts, Unclear DebtsApplicantIncomeGross applicant incomeNumerical (e.g., 5000 or 10000)LoanAmountRequested loan amount (in thousands)Numerical (e.g., 100 = $100,000)⚠️ Important Note on Loan Amount:The model expects LoanAmount expressed in thousands.For example:Enter 100 to represent $100,000 / ₹100,000Enter 50 to represent $50,000 / ₹50,000(Entering 100000 directly will be interpreted by the model as 100 million, leading to high rejection rates).🔌 API Reference1. Browser GET Request (Query Parameters)PlaintextGET /prediction?Gender=Male&Married=Married&Credit_History=Clear Debts&ApplicantIncome=10000&LoanAmount=100
2. Programmatic POST Request (JSON Payload)Endpoint: POST http://localhost:5000/predictionHeaders: Content-Type: application/jsonRequest Body:JSON{
  "Gender": "Male",
  "Married": "Married",
  "Credit_History": "Clear Debts",
  "ApplicantIncome": 10000,
  "LoanAmount": 100
}
Response:JSON{
  "Loan_Approval_Status": "Approved"
}
🛠️ Local Development & TestingIf you prefer running the source code locally without Docker:Clone the repository:Bashgit clone [https://github.com/sanasheikh01206-bot/loan-approval-mlops.git](https://github.com/sanasheikh01206-bot/loan-approval-mlops.git)
cd loan-approval-mlops
Create and activate a virtual environment:Bashpython -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate          # On Windows
Install dependencies:Bashpip install -r requirements.txt
Run the automated unit tests:Bashpytest
Start the local Flask server:Bashpython app.py
🚀 CI/CD Pipeline SummaryTesting: Every commit or pull request triggers automated endpoint validation with pytest.Container Registry: Merges to main authenticate via Docker Hub tokens, build a multi-platform Docker image, and push to sana01206/loan-approval-mlops:latest.Zero-Downtime Deployment Ready: The generated Docker image can be deployed directly to cloud container environments like Render, AWS ECS, or GCP Cloud Run.

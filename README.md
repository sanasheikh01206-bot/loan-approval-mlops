# End-to-End Loan Approval Prediction API

An automated end-to-end Machine Learning web service built to assess and predict loan eligibility based on applicant financial and demographic profiles. The application packages a Scikit-Learn classification pipeline into a production-ready Flask RESTful API, fully containerized and configured for automated continuous deployment to Render.

---

## 📌 Project Overview

Manual loan approval workflows can be slow, resource-intensive, and prone to inconsistent risk evaluation. This project automates the risk screening process by exposing a lightweight, robust inference API powered by a pre-trained machine learning model.

The service accepts structured applicant payloads over standard HTTP methods, applies all necessary transformations dynamically, and outputs instant classification results (`Approved` vs. `Rejected`) alongside inference diagnostics and API health telemetry.

---

## 🔬 Model Training & Workflow

The model development workflow was designed and verified through an iterative training notebook before being packaged for serving:

1. **Exploratory Data Analysis (EDA):**
   - Investigated feature distributions across key applicant criteria including income levels, loan term durations, and credit records.
   - Identified and handled missing values across both categorical (e.g., Dependents, Self-Employed status) and numerical fields (e.g., Loan Amount, Credit History).

2. **Feature Engineering & Preprocessing:**
   - **Numerical Transformations:** Addressed skewness in financial parameters (such as `ApplicantIncome`, `CoapplicantIncome`, and `LoanAmount`) using normalization/scaling techniques to balance variance. Note that `LoanAmount` is normalized to thousands to match standard industry reporting conventions.
   - **Categorical Encoding:** Encoded demographic and qualification attributes (Gender, Married, Education, Property Area) using consistent one-hot and binary encoding schemes.
   - **Critical Predictors:** Feature importance analysis established `Credit_History` as the most influential signal determining approval probability, paired closely with debt-to-income indicators.

3. **Model Selection & Evaluation:**
   - Evaluated multiple classification architectures (including Logistic Regression, Decision Trees, and Random Forest Classifiers) using cross-validation.
   - Tuned hyperparameters to balance precision and recall, optimizing specifically to prevent false approvals (minimizing default risk).
   - Exported the fitted estimator and preprocessing pipeline using `pickle` / `joblib` artifacts to ensure reproducible inference inside the production backend.

---

## 🛠️ Tech Stack & Tools

- **Language:** Python 3.10+
- **Machine Learning & Data Processing:** Scikit-Learn, Pandas, NumPy
- **API Framework:** Flask, Werkzeug
- **Environment & Experimentation:** Google Colab, Jupyter Notebook
- **Containerization:** Docker
- **Testing & Quality Assurance:** PyTest
- **Deployment Platform:** Render

---

## 📂 Project Directory Structure

```text
loan-approval-api/
│
├── .github/
│   └── workflows/
│       └── automate.yml             # Automated CI/CD test and deployment pipeline
│
├── model/
│   ├── loan_model.pkl            # Serialized Scikit-Learn model artifact
│   └── notebooks/
│       └── model_training.ipynb  # Colab training, EDA, and validation notebook
│
├── static/                       # Optional assets
├── templates/
│   └── index.html                # Basic API test interface
│
├── app.py                        # Core Flask API entrypoint and route handlers
├── Dockerfile                    # Container configuration file
├── requirements.txt              # Production Python dependencies
├── Procfile                      # Render process file
├── test_app.py                   # Automated endpoint unit tests (PyTest)
└── README.md                     # Documentation

## 📝 **Input Features & Guidelines**

| Feature | Description | Accepted Values / Format |
| :--- | :--- | :--- |
| **Gender** | Applicant gender | `Male`, `Female` |
| **Married** | Applicant marital status | `Married`, `Unmarried` |
| **Credit_History** | Prior credit standing | `Clear Debts`, `Unclear Debts` |
| **ApplicantIncome** | Gross applicant income | Numerical (e.g., `5000` or `10000`) |
| **LoanAmount** | Requested loan amount (**in thousands**) | Numerical (e.g., `100` = $100,000) |

> ⚠️ **Important Note on Loan Amount:**  
> The model expects `LoanAmount` expressed **in thousands**.  
> *For example:*  
> * Enter **`100`** to represent **$100,000 / ₹100,000**  
> * Enter **`50`** to represent **$50,000 / ₹50,000**  
> *(Entering `100000` directly will be interpreted by the model as 100 million, leading to high rejection rates).*

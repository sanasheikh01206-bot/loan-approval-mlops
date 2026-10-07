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

### 2. Run the container
```bash
docker run -d -p 5000:5000 --name loan-app sana01206/loan-approval-mlops:latest

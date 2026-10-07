import os
import pickle
from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

# Load model safely using absolute file path
model_path = os.path.join(os.path.dirname(__file__), "classifier.pkl")
with open(model_path, "rb") as f:
    clf = pickle.load(f)


@app.route("/", methods=["GET"])
def root():
    return render_template("index.html")

    


@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    """Predict loan status via browser query params (GET) or JSON body (POST)."""
    if request.method == "GET":
        data = request.args
    else:
        data = request.get_json(force=True)

    gender = 0 if data.get("Gender") == "Male" else 1
    married = 0 if data.get("Married") == "Unmarried" else 1
    credit = 0 if data.get("Credit_History") == "Unclear Debts" else 1
    income = float(data.get("ApplicantIncome", 0))
    loan = float(data.get("LoanAmount", 0))

    result = clf.predict([[gender, married, income, loan, credit]])
    pred = "Rejected" if result[0] == 0 else "Approved"

    return jsonify({"loan_approval_status": pred})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# 🍷 Universal Regression AI Factory

A modular, configuration-driven end-to-end Machine Learning pipeline for Regression tasks. 

## 🚀 The Architecture
This project follows an industrial-grade modular structure, decoupling data ingestion, validation, transformation, training, and evaluation.

### Key Features:
* **Modular Pipeline:** 5-stage automated workflow.
* **Config-Driven:** Control everything via `config.yaml` and `params.yaml`.
* **Logging & Exceptions:** Custom logging and error handling for production stability.
* **Flask API:** Real-time prediction interface.

## 🛠️ Installation
1. Clone the repo: `git clone <your-repo-link>`
2. Create VENV: `python -m venv venv`
3. Activate VENV: `venv\Scripts\activate`
4. Install: `pip install -r requirements.txt`

## 🏃 Usage
* **Run Training:** `python main.py`
* **Launch Web App:** `python app.py` (Visit localhost:8080)
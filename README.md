# 🛡️ PhishGuard: Phishing Attack Detection System

Phishing attacks remain one of the most widespread and damaging cybersecurity threats. Whether it’s a fake email or a malicious URL, users often fall victim to deceptive tactics. **PhishGuard** is a web-based detection system built to combat this — offering real-time scanning of emails and URLs using a **hybrid Deep Learning + NLP model**.

---

## 🚀 Features

- 🔐 Secure user authentication with Flask-Login, hashed passwords, and token-based email reset
- 📧 Email phishing detection from `.eml` files using a CNN + BiLSTM hybrid model
- 🔗 URL phishing detection using TF-IDF and handcrafted features via dense neural networks
- 📊 Admin dashboard with usage logs, feedback tracking, and scan statistics
- 📥 User dashboard with scan history, interactive charts, and result breakdowns
- 🔁 Feedback loop system to enhance model accuracy over time
- ⚙️ Modular three-layer architecture: Presentation, Application, Data

---

## 🖼️ User Interface

- Built with **HTML**, **CSS**, **Bootstrap 5**
- Interactive, real-time scanning via **AJAX**
- Dashboard visualizations for both users and admins

---

## 🧠 Machine Learning Overview

| Scanner        | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Email**      | NLP preprocessing → CNN + BiLSTM model → Verdict + Confidence              |
| **URL**        | Handcrafted features (87) + TF-IDF vectorization → Meta-classifier         |
| **Inference**  | Real-time model predictions with probability confidence score              |

---

## 🗄️ Tech Stack

| Layer            | Technologies Used                                 |
|------------------|---------------------------------------------------|
| Frontend         | HTML, CSS, Bootstrap 5, JavaScript, AJAX          |
| Backend          | Python, Flask, Flask-Login, SQLAlchemy            |
| Database         | SQLite + SQLAlchemy ORM                           |
| ML/DL Frameworks | PyTorch, scikit-learn, joblib                     |

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
Flask==2.3.2
Flask-Login==0.6.3
Flask-SQLAlchemy==3.1.1
scikit-learn==1.5.0
joblib==1.5.1
gunicorn
```
## 📂 Project Structure
``` bash
phishguard/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── models/                    # Saved ML/DL model files
│   ├── email_cnn_bilstm.pkl
│   └── url_meta_classifier.pkl
├── utils/                     # Preprocessing and inference modules
│   ├── email_model.py
│   ├── url_model.py
│   └── preprocessing.py
├── routes/                    # Flask Blueprints
│   ├── auth.py
│   ├── email_scan.py
│   └── url_scan.py
├── templates/                 # HTML files
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
├── static/                    # Static files (CSS, JS, Images)
│   ├── js/
│   └── css/
└── database/                  # SQLite DB and ORM models
    └── models.py
```
## How It Works
- User uploads an .eml file or pastes a URL
- Backend extracts features and processes data
- Model performs inference and returns a verdict (Phishing or Legitimate) with confidence
- Dashboard displays the result visually
- User can submit feedback, which is stored for retraining

## Future Improvements
- 🌐 Support for multilingual phishing content
- 🔁 Continuous online retraining from real-time feedback
- ☁️ Deployment to Heroku/AWS with CI/CD pipelines
- 📤 SMTP gateway integration for email scanning at source

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import os, random, time

# ─── INIT ─────────────────────────────────────────────────
app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["SECRET_KEY"] = "change-this-to-something-random"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/phishguard.db"
db = SQLAlchemy(app)

# ─── USER MODEL ───────────────────────────────────────────
class User(UserMixin, db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    email   = db.Column(db.String(150), unique=True, nullable=False)
    pw_hash = db.Column(db.String(256), nullable=False)

# ─── LOGIN MANAGER ────────────────────────────────────────
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ─── ROUTES ───────────────────────────────────────────────

# Home/dashboard (protected)
@app.route("/")
@login_required
def dashboard():
    return render_template("dashboard.html")

# Email scanner page (protected)
@app.route("/email")
@login_required
def email_page():
    return render_template("scan_email.html")

# URL scanner page (protected)
@app.route("/url")
@login_required
def url_page():
    return render_template("scan_url.html")

# ---- Mock prediction logic for both APIs ----
def fake_prediction():
    verdict = random.choice(["Phishing", "Legitimate"])
    conf    = round(random.uniform(0.6, 0.95), 2)
    time.sleep(0.3)
    return verdict, conf

@app.post("/api/email")
def api_email():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file"}), 400
    verdict, conf = fake_prediction()
    return jsonify({"verdict": verdict, "confidence": conf})

@app.post("/api/url")
def api_url():
    if not request.is_json:
        return jsonify({"error": "Bad request"}), 400
    verdict, conf = fake_prediction()
    return jsonify({"verdict": verdict, "confidence": conf})

# ─── AUTH ROUTES ──────────────────────────────────────────

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"].lower()
        pw = request.form["password"]
        if User.query.filter_by(email=email).first():
            flash("Email already registered", "danger")
            return redirect(url_for('register'))
        user = User(email=email, pw_hash=generate_password_hash(pw))
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('dashboard'))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].lower()
        pw = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.pw_hash, pw):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash("Invalid credentials", "danger")
        return redirect(url_for('login'))
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# ─── MAIN ─────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)

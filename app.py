from flask import Flask, render_template

# Tell Flask where to find templates & static files
app = Flask(__name__, template_folder="templates", static_folder="static")

# ─── ROUTES ───────────────────────────────────────────────
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/email")
def email_page():
    return "<h3>Email Scanner (coming soon)</h3>"

@app.route("/url")
def url_page():
    return "<h3>URL Scanner (coming soon)</h3>"

# ─── MAIN ─────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import random, time


# Tell Flask where to find templates & static files
app = Flask(__name__, template_folder="templates", static_folder="static")

# ─── ROUTES ───────────────────────────────────────────────
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/email")
def email_page():
    return render_template("scan_email.html")
# ---- MOCK prediction API (will swap with real ML later) ----
def fake_prediction():
    verdict = random.choice(["Phishing", "Legitimate"])
    conf    = round(random.uniform(0.6, 0.95), 2)
    time.sleep(0.3)          # tiny delay so it feels real
    return verdict, conf
@app.post("/api/email")
def api_email():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file"}), 400
    # here you'd parse file.read() with email.parser in future
    verdict, conf = fake_prediction()
    return jsonify({"verdict": verdict, "confidence": conf})

@app.route("/url")
def url_page():
    return render_template("scan_url.html")
@app.post("/api/url")
def api_url():
    if not request.is_json:
        return jsonify({"error": "Bad request"}), 400
    verdict, conf = fake_prediction()
    return jsonify({"verdict": verdict, "confidence": conf})


# ─── MAIN ─────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)

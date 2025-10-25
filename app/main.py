from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "JR-9 Turbo - Online ✅"

@app.route("/status")
def status():
    return {"status": "running", "version": "free-tier"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

from flask import Flask, request, jsonify
import os
import sys
import json
from datetime import datetime

app = Flask(__name__)

SYNC_TOKEN = os.getenv("RENDER_SYNC_TOKEN", "").strip()

def auth_ok(req):
    if not SYNC_TOKEN:
        return True
    return req.headers.get("X-JR9-Token", "") == SYNC_TOKEN

@app.route("/")
def home():
    return "JR-9 Turbo - Online ✅"

@app.route("/status")
def status():
    return {"status": "running", "version": "free-tier", "ts": datetime.utcnow().isoformat() + "Z"}

@app.route("/sync", methods=["GET", "POST"])
def sync():
    if not auth_ok(request):
        return jsonify({"ok": False, "error": "unauthorized"}), 401

    if request.method == "GET":
        return jsonify({"ok": True, "mode": "GET", "ts": datetime.utcnow().isoformat() + "Z"})

    payload = request.get_json(silent=True) or {}
    print("[SYNC] payload:", json.dumps(payload, ensure_ascii=False), file=sys.stdout, flush=True)
    return jsonify({"ok": True, "mode": "POST", "received": payload, "ts": datetime.utcnow().isoformat() + "Z"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

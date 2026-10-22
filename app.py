import os
import hmac

from flask import Flask, request, jsonify

app = Flask(__name__)

WEBHOOK_TOKEN = os.environ.get("WEBHOOK_TOKEN", "")


@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "running"}), 200


@app.route("/webhook", methods=["POST"])
def receive_webhook():
    supplied_token = request.headers.get("X-Webhook-Token", "")

    if not WEBHOOK_TOKEN or not hmac.compare_digest(
        supplied_token,
        WEBHOOK_TOKEN
    ):
        return jsonify({"error": "Unauthorized"}), 401

    payload = request.get_json(silent=True)

    if payload is None:
        return jsonify({"error": "Expected JSON payload"}), 400

    app.logger.info("Webhook received successfully")

    # Process the event here.
    # Avoid logging sensitive payloads.

    return jsonify({"status": "accepted"}), 200

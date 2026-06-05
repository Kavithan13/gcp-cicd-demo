import os
from flask import Flask, render_template, request

# PR test commit
app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "admin123"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        return render_template('home.html', username=username)

    return "Invalid Credentials"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

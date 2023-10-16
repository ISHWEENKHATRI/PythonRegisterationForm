from flask import Flask, request, render_template

app = Flask(__name__)

# A simple in-memory user store (replace with a database in a real app)
users = {}

@app.route('/')
def home():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    name = request.form.get('name')
    phone = request.form.get('phone')
    
    if username in users:
        return 'Username already taken. Try another one.'
    
    users[username] = {'password': password, 'name': name, 'phone': phone}
    return f'Registration successful for {username}.'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

user = {
    "Navadeep": "Deepu2005R",
    "Sirisha" : "lmao"
}

@app.route('/Login', methods = ['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if username in user and user[username] == password:
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password'})
    
if (__name__ == "__main__"):
    app.run(debug=True)
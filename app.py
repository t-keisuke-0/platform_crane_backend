from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=[
    "http://localhost:3000",
    "https://platform-crane-frontend.onrender.com"
]) # 許可するオリジンを指定

@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({'message': f'Hello, {name}!'})

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({'you_sent': data})

# if __name__ == '__main__':
#     app.run(debug=True)

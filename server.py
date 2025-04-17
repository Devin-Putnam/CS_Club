from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow cross-origin requests from extension

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello from Python!'})

if __name__ == '__main__':
    app.run(debug=True)

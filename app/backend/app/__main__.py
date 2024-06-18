from flask import Flask, request, jsonify
from flask_cors import CORS

HOST = '0.0.0.0'
PORT = 8081

app = Flask(__name__)
CORS(app)

if __name__=="__main__":
    app.run(host=HOST, port= PORT)
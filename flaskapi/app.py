import json
from flask import Flask, render_template, send_from_directory, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'OK': '200 OK'}), 200

if __name__ == "__main__":
    app.run()

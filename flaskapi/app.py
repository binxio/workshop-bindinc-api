import json
from flask import Flask, render_template, send_from_directory, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'OK': '200 OK'}), 200

@app.route('/similarity', methods=['POST'])
def get_similarity():
    output = {"status": "Pretending to have processed your data and returning this result."}
    return jsonify(output), 200

if __name__ == "__main__":
    app.run()

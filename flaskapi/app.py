import base64
import json
import os
import uuid
import subprocess
import vertexai
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings.vertexai import VertexAIEmbeddings
from flask import Flask, render_template, send_from_directory, request, jsonify

app = Flask(__name__)

embeddings = VertexAIEmbeddings(
    model_name="textembedding-gecko-multilingual@latest",
    chunk_size=1
)

store = FAISS.load_local("data/index",embeddings,"index")

@app.route('/')
def home():
    return jsonify({'OK': '200 OK'}), 200

@app.route('/similarity', methods=['POST'])
def get_similarity():
    # Get the JSON data from POST request
    data = request.get_json()

    # Ensure the data contains a 'query' key
    if not data or 'query' not in data:
        return jsonify({'error': 'Missing query parameter'}), 400

    query = data['query']
    result = store.similarity_search(query)

    output = [{"chunk": r.page_content, "metadata": r.metadata} for r in result]
    return jsonify(output), 200

if __name__ == "__main__":
    app.run()

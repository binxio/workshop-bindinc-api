import json
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings.vertexai import VertexAIEmbeddings
from flask import Flask, render_template, send_from_directory, request, jsonify

app = Flask(__name__)

# Load the vector database
embeddings = VertexAIEmbeddings(
    model_name="textembedding-gecko-multilingual@latest",
    chunk_size=1
)

store = FAISS.load_local("data/index", embeddings, "index")

@app.route('/')
def home():
    return jsonify({'OK': '200 OK'}), 200

# Still serve mock response
@app.route('/similarity', methods=['POST'])
def get_similarity():
    output = {"status": "Pretending to have processed your data and returning this result."}
    return jsonify(output), 200

if __name__ == "__main__":
    app.run()

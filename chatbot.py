from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load language model for text generation
text_generator = pipeline("text-generation", model="lmsys/fastchat-t5-3b-v1.0")

# Define endpoint to render chatbot interface
@app.route('/')
def index():
    return render_template('index.html')

# Define endpoint to handle user messages
@app.route('/message', methods=['POST'])
def get_response():
    user_message = request.json['message']

    # Generate response using language model
    response = text_generator(user_message, max_length=100)[0]['generated_text']

    # Fetch relevant source documents based on user query (implement logic)
    source_documents = fetch_source_documents(user_message)

    return jsonify({'response': response, 'documents': source_documents})

# Define function to fetch relevant source documents
def fetch_source_documents(user_query):
    # Implement logic to retrieve relevant documents based on user query
    # This could involve querying a database or calling an external API

    # Return example documents for demonstration purposes
    return [{'title': 'Document Title 1', 'link': 'https://example.com/document1'},
            {'title': 'Document Title 2', 'link': 'https://example.com/document2'}]

if __name__ == '__main__':
    app.run(debug=True)

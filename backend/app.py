from flask import Flask, request, jsonify
from model import predict_text
from database import init_db, save_prediction, get_history
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Initialize database
init_db()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_text = data.get('text', '')
    if not input_text:
        return jsonify({'error': 'No input text provided'}), 400
    
    # Get prediction from AI model
    prediction = predict_text(input_text)
    
    # Save to database
    save_prediction(input_text, prediction)
    
    return jsonify({'prediction': prediction})

@app.route('/history', methods=['GET'])
def history():
    history = get_history()
    return jsonify(history)

if __name__ == '__main__':
    app.run(debug=True)
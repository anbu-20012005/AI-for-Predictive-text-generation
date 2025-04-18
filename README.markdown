# AI for Predictive Text Generation

This project is a web application that predicts the next word in a sentence using a simple AI model.

## Prerequisites
- Python 3.8+
- Node.js 14+
- Git

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd ai-predictive-text
   ```

2. **Back End Setup**:
   - Create a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install dependencies:
     ```bash
     pip install flask flask-cors
     ```
   - Run the Flask server:
     ```bash
     python app.py
     ```

3. **Front End Setup**:
   - Place `index.html`, `App.jsx`, and `styles.css` in a directory (e.g., `frontend`).
   - Open `index.html` in a browser (use a local server like `live-server` for best results):
     ```bash
     npm install -g live-server
     live-server frontend
     ```

4. **Usage**:
   - Open the web app in your browser (e.g., `http://localhost:8080`).
   - Enter a partial sentence (e.g., "The sun is").
   - Click "Predict" to see the next word.
   - View prediction history below.

## Project Structure
- `index.html`: Front-end HTML with React setup.
- `App.jsx`: React component for UI.
- `styles.css`: Custom CSS.
- `app.py`: Flask server.
- `model.py`: AI model (Markov chain).
- `database.py`: SQLite database logic.

## Notes
- The AI model is a simple Markov chain. For better predictions, consider using Hugging Face's GPT-2 (requires `pip install transformers`).
- Expand the training data in `model.py` for improved results.

## Troubleshooting
- Ensure the Flask server is running on `http://localhost:5000`.
- Check browser console for errors if the front end fails to fetch predictions.
from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# --- 1. Initialize Flask App ---
app = Flask(__name__)

# --- 2. Load the Hugging Face Model ---
try:
    logging.info("Loading summarization model...")
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    summarizer = None

# --- 3. NEW: Add a route for the Web Interface ---
@app.route("/")
def home():
    """
    Serve the main HTML page (our user interface).
    Flask will automatically look for 'index.html' in the 'templates' folder.
    """
    return render_template("index.html")

# --- 4. Define the API Endpoint (No change from before) ---
@app.route("/summarize", methods=["POST"])
def summarize_text():
    """
    API endpoint to summarize text.
    Expects a JSON payload with a "text" key.
    """
    if summarizer is None:
        return jsonify({"error": "Model is not available"}), 500

    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "Missing 'text' key in JSON payload"}), 400

    input_text = data['text']

    if not isinstance(input_text, str) or len(input_text.strip()) == 0:
         return jsonify({"error": "'text' must be a non-empty string"}), 400

    try:
        logging.info(f"Received text. Length: {len(input_text)} chars.")
        
        summary = summarizer(
            input_text, 
            max_length=150,
            min_length=30,
            do_sample=False
        )
        
        output_summary = summary[0]['summary_text']
        
        logging.info(f"Generated summary. Length: {len(output_summary)} chars.")

        return jsonify({
            "original_length": len(input_text),
            "summary": output_summary,
            "summary_length": len(output_summary)
        })

    except Exception as e:
        logging.error(f"Error during summarization: {e}")
        return jsonify({"error": "An internal error occurred"}), 500

# --- 5. Run the Flask App (No change from before) ---
if __name__ == "__main__":
    app.run(debug=True, port=5000)
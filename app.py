from flask import Flask, jsonify
import random
import uuid
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

verdicts = ["Copyright Infringed", "No Infringement Detected", "Uncertain"]
confidence_range = (50.0, 99.9)

@app.route("/check_copyright", methods=['POST'])
def check_copyright():
    response = {
        "file_id": str(uuid.uuid4()),  # Generate a random file_id
        "verdict": random.choice(verdicts),  # Random verdict
        "confidence": round(random.uniform(*confidence_range), 1)  # Random confidence score
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
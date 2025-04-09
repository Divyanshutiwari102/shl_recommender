from flask import Flask, jsonify, request
from recommender import SHLRecommender
import pandas as pd

app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend():
    # Get parameters from the query string
    job_role = request.args.get('job_role', default=None, type=str)
    skill_level = request.args.get('skill_level', default=None, type=str)

    # Validate parameters
    if not job_role or not skill_level:
        return jsonify({"error": "Please provide both job_role and skill_level"}), 400
    
    # Initialize recommender with the dataset
    rec = SHLRecommender("assessments.csv")
    results = rec.recommend(job_role, skill_level)

    # Return results as JSON
    return jsonify(results.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
import os

if __name__ == '__main__
HEAD
    port = int(os.environ.get('PORT', 5000))  # Render will provide the PORT env variable

    port = int(os.environ.get('PORT', 5000))
 89d2af1 (Fix: Bind Flask app to 0.0.0.0 and dynamic port for Render)
    app.run(host='0.0.0.0', port=port)

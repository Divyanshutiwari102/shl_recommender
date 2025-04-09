from flask import Flask, jsonify, request
from recommender import SHLRecommender
import pandas as pd
import os

app = Flask(__name__)

# Homepage route to prevent 404
@app.route("/")
def home():
    return "SHL Recommender is running!"

# Recommendation API route
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

# ✅ Works on both local and Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render will set PORT env variable
    app.run(host='0.0.0.0', port=port, debug=True)

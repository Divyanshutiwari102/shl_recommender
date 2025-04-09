from flask import Flask, jsonify, request
from recommender import SHLRecommender
import pandas as pd
import os

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "SHL Recommender is running!"

# Recommend route
@app.route('/recommend', methods=['GET'])
def recommend():
    job_role = request.args.get('job_role', default=None, type=str)
    skill_level = request.args.get('skill_level', default=None, type=str)

    if not job_role or not skill_level:
        return jsonify({"error": "Please provide both job_role and skill_level"}), 400

    rec = SHLRecommender("assessments.csv")
    results = rec.recommend(job_role, skill_level)

    return jsonify(results.to_dict(orient='records'))

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's dynamic port if set
    app.run(host='0.0.0.0', port=port, debug=True)

from flask import Flask, jsonify, request
from recommender import SHLRecommender
import pandas as pd

app = Flask(__name__)

@app.route('/get_assessment', methods=['GET'])
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
    # Run the Flask app on port 5001
    app.run(debug=True, host='0.0.0.0', port=5001)

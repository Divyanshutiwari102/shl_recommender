from flask import Flask, jsonify, request, render_template
from recommender import SHLRecommender
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/recommend', methods=['GET'])
def recommend():
    job_role = request.args.get('job_role', default=None, type=str)
    skill_level = request.args.get('skill_level', default=None, type=str)

    if not job_role or not skill_level:
        return jsonify({"error": "Please provide both job_role and skill_level"}), 400

    rec = SHLRecommender("assessments.csv")
    results = rec.recommend(job_role, skill_level)

    return jsonify(results.to_dict(orient='records'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

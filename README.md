# 🧠 SHL Assessment Recommendation Engine

This project is a take-home assignment for the **Research Intern** position at **SHL**. It is designed to recommend suitable assessments from SHL’s product catalog based on a given **job role** and **skill level**.

---

## 🎯 Objective

Recommend SHL assessments based on:
- 🧑‍💼 **Job Role** (e.g., Analyst, Manager, Engineer)
- 📈 **Skill Level** (e.g., Entry, Mid, Senior)

---

## 🚀 Features

- 🔍 Command-Line Interface (CLI) and 📊 Streamlit Web App  
- 🧠 Simple rule-based recommendation using tags  
- 📁 Easily extendable with a larger or real SHL product catalog  
- 🐍 Clean and modular Python code

---

## 🛠️ Tech Stack

- Python 3.9  
- Streamlit  
- Pandas  
- (Optional) Scikit-learn – for advanced matching logic

---

## 📁 Project Structure

shl_recommender/ ├── app.py # Streamlit Web App
├── sample_input.py # Command-Line Interface (CLI)
├── recommender.py # Core recommendation logic
├── assessments.csv # Sample SHL product catalog
├── requirements.txt # Dependencies
└── README.md # Documentation



---

## 📊 Sample Product Catalog (`assessments.csv`)

| Assessment_ID | Assessment_Name         | Job_Role | Skill_Level | Tags                     |
|---------------|--------------------------|----------|--------------|--------------------------|
| A101          | Cognitive Ability Test   | Analyst  | Entry        | cognitive, logic         |
| A102          | Leadership Evaluation    | Manager  | Senior       | leadership, strategic    |
| A103          | Coding Skills Test       | Engineer | Mid          | coding, programming      |

---

## ⚙️ How It Works

1. User enters **Job Role** and **Skill Level**  
2. Matching assessments are filtered using tags  
3. Recommended assessments are displayed

---

## ▶️ How to Run

### 🔸 CLI Mode

```bash
python sample_input.py
🔹 Streamlit Web App
bash
python -m streamlit run app.py
Then open http://localhost:8501 in your browser.

📦 Installation
bash

# Clone the repository
git clone https://github.com/your-username/shl-recommender.git
cd shl-recommender

# (Optional) Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt
🔧 Future Improvements
Use semantic similarity with word embeddings (e.g., spaCy, BERT)

Integrate with real SHL product APIs

Add advanced filters (industry, experience, region)

📬 Contact
For questions , please contact: Divyanshu tiwari at divyanshutiwari337@gmail.com









**Title: SHL Assessment Recommender - Approach Document**

**1. Objective:**
Build a web-based tool that recommends the most relevant SHL assessments based on a candidate's job role and skill level.

**2. Dataset:**
Used a structured CSV file `assessments.csv` containing:
- Assessment ID  
- Tags  
- Target Job Roles  
- Skill Level

**3. Recommendation Logic:**
- Built a custom recommender (`SHLRecommender`) in Python.
- Filtered assessments based on:
  - Matching job roles (partial or full match).
  - Matching skill level.
  - Prioritized tag overlaps for more relevance.

**4. Tech Stack:**
- **Backend:** Flask (Python)
- **Frontend:** HTML + JavaScript (basic form)
- **Hosting:** Render.com
- **Repository:** [GitHub Link](https://github.com/Divyanshutiwari102/shl_recommender)

**5. Features:**
- `/recommend` API for programmatic access.
- Homepage with a simple form to test recommendations.
- JSON response of relevant assessments.

**6. Deployment:**
- Deployed using Render's web service.
- Supports both API access and browser-based interaction.

**7. How to Use:**
- Visit: `https://shl-recommender-2-u5ki.onrender.com/`
- Enter job role and skill level to get assessment recommendations.


import streamlit as st
import requests

st.title("SHL Assessment Recommender")

job_role = st.text_input("Enter Job Role (e.g., Analyst, Manager)")
skill_level = st.selectbox("Select Skill Level", ["Entry", "Mid", "Senior"])

if st.button("Get Recommendations"):
    if not job_role or not skill_level:
        st.warning("Please enter both job role and skill level.")
    else:
        try:
            api_url = f"http://127.0.0.1:5000/recommend?job_role={job_role}&skill_level={skill_level}"
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            st.write("🔍 Raw API Response:", data)

            if data:
                st.success("Recommended Assessments:")
                for item in data:
                    assessment_id = item.get('assessment_id', 'N/A')
                    tags = item.get('tags', 'N/A')
                    target_roles = item.get('target_job_roles', 'N/A')
                    st.write(f"- **{assessment_id}**: {tags} (Target: {target_roles})")
            else:
                st.info("No assessments found for the given inputs.")

        except requests.exceptions.RequestException as e:
            st.error(f"API Error: {e}")
        except ValueError:
            st.error("Invalid response from API.")

import streamlit as st
import requests  # We'll use requests to call the API

st.title("SHL Assessment Recommender")

job_role = st.text_input("Enter Job Role (e.g., Analyst, Manager)")
skill_level = st.selectbox("Select Skill Level", ["Entry", "Mid", "Senior"])

if st.button("Recommend"):
    # API call to Flask app for recommendations
    if job_role and skill_level:
        api_url = f"http://127.0.0.1:5001/get_assessment?job_role={job_role}&skill_level={skill_level}"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            recommendations = response.json()
            # Convert to a dataframe and display it
            st.dataframe(recommendations)
        else:
            st.error(f"Error: {response.json()['error']}")
    else:
        st.warning("Please enter both Job Role and Skill Level")

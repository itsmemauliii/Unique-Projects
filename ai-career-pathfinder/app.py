import streamlit as st
import json
from scripts.ai_engine import suggest_careers

# Load career paths
with open("data/career_paths.json", "r") as file:
    career_data = json.load(file)

# App layout
st.set_page_config(page_title="AI Career Path Finder", layout="wide")

st.title("🚀 AI Career Path Finder")
st.write("Get personalized career recommendations based on your skills and interests!")

# User input
skills = st.text_area("Enter your skills (comma-separated):")
interests = st.text_area("Enter your interests (comma-separated):")

# Get recommendations
if st.button("Find Career Path"):
    if skills and interests:
        recommendations = suggest_careers(skills, interests, career_data)
        st.success("Here are the best career paths for you:")
        for career, confidence in recommendations:
            st.write(f"🌟 **{career}** - Match Score: {confidence}%")
    else:
        st.warning("Please enter both skills and interests.")

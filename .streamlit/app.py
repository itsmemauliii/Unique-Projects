import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample food data
food_data = pd.DataFrame({
    "Food": ["Oats", "Chicken Breast", "Almonds", "Broccoli", "Rice", "Eggs"],
    "Calories": [68, 165, 575, 55, 130, 78],
    "Proteins": [2.4, 31, 21, 3.7, 2.7, 6],
    "Carbs": [12, 0, 20, 11, 28, 0.6],
    "Fats": [1.4, 3.6, 49, 0.5, 0.3, 5]
})

# App title
st.title("Personalized Diet Recommendation System")

# User inputs
st.sidebar.header("Enter Your Details:")
age = st.sidebar.number_input("Age (years)", min_value=10, max_value=100, value=25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=150, value=70)
height = st.sidebar.number_input("Height (cm)", min_value=100, max_value=220, value=170)
activity_level = st.sidebar.selectbox("Activity Level", ["Sedentary", "Lightly active", "Moderately active", "Very active"])

diet_type = st.sidebar.selectbox("Dietary Preference", ["No preference", "Vegetarian", "Vegan"])
allergies = st.sidebar.multiselect("Food Allergies", food_data["Food"].unique())

# BMR calculation
if gender == "Male":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
else:
    bmr = 10 * weight + 6.25 * height - 5 * age - 161

activity_multiplier = {"Sedentary": 1.2, "Lightly active": 1.375, "Moderately active": 1.55, "Very active": 1.725}
daily_calories = bmr * activity_multiplier[activity_level]

st.sidebar.subheader(f"Daily Calorie Requirement: {int(daily_calories)} kcal")

# Filter food data
filtered_food = food_data[~food_data["Food"].isin(allergies)]

# Generate a meal plan
meal_plan = filtered_food.sample(n=4).reset_index(drop=True)

# Display meal plan
st.header("Your Personalized Meal Plan:")
for i, row in meal_plan.iterrows():
    st.write(f"**{row['Food']}** - {row['Calories']} kcal")

# Nutrient distribution
nutrient_summary = meal_plan[["Proteins", "Carbs", "Fats"]].sum()

# Visualization
st.header("Nutrient Distribution:")
fig, ax = plt.subplots()
ax.pie(nutrient_summary, labels=nutrient_summary.index, autopct='%1.1f%%', startangle=140)
ax.axis('equal')
st.pyplot(fig)

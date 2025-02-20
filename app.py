import streamlit as st
import pandas as pd

# Load the recipe data (If you have a CSV, replace 'recipes.csv' with your file)
df = pd.read_csv("recipes.csv")  

# Streamlit UI
st.title("AI-Powered Recipe Finder 🍽️")
st.write("Find the best recipes based on your available ingredients!")

# Display recipes
for index, row in df.iterrows():
    st.subheader(row["Recipe Name"])
    st.write("**Ingredients:**", row["Ingredients"])

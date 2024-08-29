import streamlit as st
import math

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / ((height/100) ** 2)

# Function to get BMI category
def get_bmi_category(bmi):
    if bmi < 16:
        return "Severe Thinness", "#FF0000"
    elif 16 <= bmi < 17:
        return "Moderate Thinness", "#FF4500"
    elif 17 <= bmi < 18.5:
        return "Mild Thinness", "#FF8C00"
    elif 18.5 <= bmi < 25:
        return "Normal", "#008000"
    elif 25 <= bmi < 30:
        return "Overweight", "#FFFF00"
    elif 30 <= bmi < 35:
        return "Obese Class I", "#FFA500"
    elif 35 <= bmi < 40:
        return "Obese Class II", "#FF6347"
    else:
        return "Obese Class III", "#FF0000"

# Streamlit UI

# Custom CSS to set the background color
st.markdown(f"""
<style>
    /* Set the background image for the entire app */
    .stApp {{
        background-color:rgb(255, 128, 0);
        background-size: 1300px;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    
    </style>
""", unsafe_allow_html=True)

st.title("BMI Calculator - Metric Units")

height = st.number_input("Enter your height (cm):", min_value=0.0, format="%.2f")
weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")

if st.button("Calculate"):
    if height > 0:
        bmi = calculate_bmi(weight, height)
        category, color = get_bmi_category(bmi)
        st.markdown(f"## Your BMI is: **{bmi:.2f}**")
        st.markdown(f"### You are in the category: **{category}**")

        # Display BMI classification table
        st.markdown("""
        ### BMI Classification Table
        | **Classification**   | **BMI range (kg/m²)** |
        |----------------------|-----------------------|
        | Severe Thinness       | < 16                  |
        | Moderate Thinness     | 16 - 17               |
        | Mild Thinness         | 17 - 18.5             |
        | Normal                | 18.5 - 25             |
        | Overweight            | 25 - 30               |
        | Obese Class I         | 30 - 35               |
        | Obese Class II        | 35 - 40               |
        | Obese Class III       | > 40                  |
        """)
       
                
    else:
        st.error("Height must be greater than zero.")

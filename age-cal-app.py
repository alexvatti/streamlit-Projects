import streamlit as st
from datetime import datetime
from datetime import datetime, date

# Title of the app
# Custom CSS to set the background color
st.markdown(f"""
<style>
    /* Set the background image for the entire app */
    .stApp {{
        background-color:rgb(149, 201, 126);
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    
    </style>
""", unsafe_allow_html=True)

st.title("Age Calculator")

# Input: Date of Birth
dob = st.date_input("Date of Birth",min_value=date(1950, 1, 1))

# Input: Today's Date
today = st.date_input("Today's Date", datetime.today())

# Calculate age
if dob and today:
    # Ensure today is not before dob
    if today >= dob:
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        st.write(f"Your age is: {age} years")
    else:
        st.write("Today's date cannot be before the date of birth.")

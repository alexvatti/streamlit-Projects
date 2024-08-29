import streamlit as st
import numpy as np

# Title of the app
st.markdown(f"""
<style>
    /* Set the background image for the entire app */
    .stApp {{
        background-color:rgb(174, 191, 62);
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    
    </style>
""", unsafe_allow_html=True)

st.title("Home Loan EMI Calculator")

# Loan Amount Slider
loan_amount = st.slider("Loan Amount (₹)", min_value=100000, max_value=10000000, step=100000, value=1000000)

# Tenure Slider
tenure_years = st.slider("Tenure (Years)", min_value=1, max_value=30, value=15)

# Interest Rate Input
interest_rate = st.slider("Interest Rate (% P.A.)", min_value=1, max_value=15, step=1, value=7)

# Calculate EMI
tenure_months = tenure_years * 12
monthly_interest_rate = (interest_rate / 100) / 12

if monthly_interest_rate > 0:
    emi = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure_months / ((1 + monthly_interest_rate) ** tenure_months - 1)
else:
    emi = loan_amount / tenure_months

total_payment = emi * tenure_months
total_interest = total_payment - loan_amount

# Display results
st.subheader("Calculation Results")

st.write(f"**Monthly EMI:** ₹{emi:.2f}")
st.write(f"**Total Amount Payable:** ₹{total_payment:.2f}")
st.write(f"**Total Interest Amount:** ₹{total_interest:.2f}")
st.write(f"**Principal Amount:** ₹{loan_amount:.2f}")

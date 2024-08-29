import streamlit as st

# SIP Calculation Function
def calculate_sip(P, i, n):
    M = P * (((1 + i) ** n - 1) / i) * (1 + i)
    return M

# Streamlit UI
# Custom CSS to set the background color
st.markdown(f"""
<style>
    /* Set the background image for the entire app */
    .stApp {{
        background-color:rgb(211, 211, 211);
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    
    </style>
""", unsafe_allow_html=True)
st.title("SIP Calculator")

# User inputs using sliders
P = st.slider("Select the amount you invest at regular intervals (P):", min_value=500, max_value=100000, step=500, value=5000)
i = st.slider("Select the expected return rate per annum (in %):", min_value=1, max_value=30, step=1, value=12)
n = st.slider("Select the time period (in years):", min_value=1, max_value=40, step=1, value=10)

# Convert annual interest rate to monthly and then to decimal
monthly_rate = i / 12 / 100
n_payments = n * 12

if st.button("Calculate Maturity Amount"):
    M = calculate_sip(P, monthly_rate, n_payments)
    total_invested = P * n_payments
    estimated_returns = M - total_invested
    
    st.markdown("## SIP Investment Summary")
    st.markdown(f"**Amount Invested at Regular Intervals (P):** ₹{P:.2f}")
    st.markdown(f"**Total Amount Invested:** ₹{total_invested:.2f}")
    st.markdown(f"**Estimated Returns:** ₹{estimated_returns:.2f}")
    st.markdown(f"**Maturity Amount (M):** ₹{M:.2f}")


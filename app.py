# app.py

import streamlit as st
from calculator import calculate_future_value, calculate_required_monthly_contribution

st.title('Investing Calculator')

# User inputs
target_amount_today = st.number_input('Target Amount Today (€)', value=250000)
initial_investment = st.number_input('Initial Investment (€)', value=10000)
inflation_rate = st.number_input('Annual Inflation Rate (%)', value=4.0) / 100
annual_interest_rate = st.number_input('Annual Interest Rate (%)', value=5.0) / 100
years = st.number_input('Number of Years', value=30)

# Calculate the future value of the target amount
target_amount_2054 = calculate_future_value(target_amount_today, inflation_rate, years)

# Calculate the required monthly contribution
required_monthly_contribution = calculate_required_monthly_contribution(target_amount_2054, initial_investment, annual_interest_rate, years)

# Display the results
st.write(f"Your target amount in future is: €{target_amount_2054:.2f}")
st.write(f"To achieve your target you should monthly contribute to buying ETF with {annual_interest_rate * 100}% interest rate: €{required_monthly_contribution:.2f}")

# app.py

import streamlit as st
from calculator import calculate_future_value, calculate_required_monthly_contribution

st.title('Investing Calculator')

# User inputs
target_amount_today = st.number_input('Target Amount Today (€)', value=300000)
initial_investment = st.number_input('Initial Investment (€)', value=10000)
inflation_rate = st.number_input('Annual Inflation Rate (%)', value=4.0) / 100
years = st.number_input('Number of Years', value=30)

# Annual interest rates
annual_interest_rate_pesimistic = st.number_input('Pesimistic Annual Interest Rate (%)', value=5.0) / 100
annual_interest_rate_realistic = st.number_input('Realistic Annual Interest Rate (%)', value=7.0) / 100
annual_interest_rate_optimistic = st.number_input('Optimistic Annual Interest Rate (%)', value=9.0) / 100

# Calculate the future value of the target amount
target_amount_2054 = calculate_future_value(target_amount_today, inflation_rate, years)

# Calculate the required monthly contributions
required_monthly_contribution_pesimistic = calculate_required_monthly_contribution(target_amount_2054, initial_investment, annual_interest_rate_pesimistic, years)
required_monthly_contribution_realistic = calculate_required_monthly_contribution(target_amount_2054, initial_investment, annual_interest_rate_realistic, years)
required_monthly_contribution_optimistic = calculate_required_monthly_contribution(target_amount_2054, initial_investment, annual_interest_rate_optimistic, years)

# Display the results
st.write(f"Your target amount in future is: €{target_amount_2054:.2f}")
st.write(f"To achieve PESIMISTIC target, you should monthly contribute to buying ETF with 5% interest rate: €{required_monthly_contribution_pesimistic:.2f}")
st.write(f"To achieve REALISTIC target, you should monthly contribute to buying ETF with 7% interest rate: €{required_monthly_contribution_realistic:.2f}")
st.write(f"To achieve OPTIMISTIC target, you should monthly contribute to buying ETF with 9% interest rate: €{required_monthly_contribution_optimistic:.2f}")


#streamlit run app.py

# calculator.py

# Define the function to calculate future value of a target amount considering inflation
def calculate_future_value(target_amount_today, inflation_rate, years):
    return target_amount_today * ((1 + inflation_rate) ** years)

# Define the function to calculate the required monthly contribution
def calculate_required_monthly_contribution(target_amount_2054, initial_investment, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12
    months = years * 12
    # Calculate the future value of the initial investment
    fv_initial = initial_investment * (1 + annual_interest_rate) ** years
    # Calculate the future value needed from monthly contributions
    fv_needed_from_contributions = target_amount_2054 - fv_initial
    # Calculate the required monthly contribution
    monthly_contribution = fv_needed_from_contributions * (monthly_interest_rate) / ((1 + monthly_interest_rate) ** months - 1)
    return monthly_contribution

if __name__ == "__main__":
    # Define the parameters
    target_amount_today = 250000  # EUR
    inflation_rate = 0.04  # 4%
    annual_interest_rate_pesimistic = 0.05  # 5%
    annual_interest_rate_realistic = 0.07  # 7%
    annual_interest_rate_optimistic = 0.09  # 9%
    years = 30
    initial_investment = 10000  # EUR

    # Calculate the future value of the target amount
    target_amount_2054 = calculate_future_value(target_amount_today, inflation_rate, years)

    # Calculate the required monthly contribution at 5% annual interest rate
    required_monthly_contribution_pesimistic = calculate_required_monthly_contribution(target_amount_2054, initial_investment, annual_interest_rate_pesimistic, years)

    # Calculate the required monthly contribution at 7% annual interest rate
    required_monthly_contribution_realistic = calculate_required_monthly_contribution(target_amount_2054, initial_investment, annual_interest_rate_realistic, years)

    # Calculate the required monthly contribution at 9% annual interest rate
    required_monthly_contribution_optimistic = calculate_required_monthly_contribution(target_amount_2054, initial_investment, annual_interest_rate_optimistic, years)

    # Print statements with f-strings
    print(f"Your target amount in future is: €{target_amount_2054:.2f}")
    print(f"To achieve PESIMISTIC target, you should monthly contribute to buying ETF with 5% interest rate: €{required_monthly_contribution_pesimistic:.2f}")
    print(f"To achieve REALISTIC target, you should monthly contribute to buying ETF with 7% interest rate: €{required_monthly_contribution_realistic:.2f}")
    print(f"To achieve OPTIMISTIC target, you should monthly contribute to buying ETF with 9% interest rate: €{required_monthly_contribution_optimistic:.2f}")

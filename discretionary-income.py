def calculate_discretionary_income(revenue_expenses):
    total_revenue = sum(amount for _, amount in revenue_expenses if amount > 0)
    total_expenses = sum(amount for _, amount in revenue_expenses if amount < 0)
    discretionary_income = total_revenue + total_expenses
    return discretionary_income
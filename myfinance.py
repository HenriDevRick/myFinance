def calculate_net_pay():
    hourly_wage = float(input("What is your hourly wage? "))
    hours_worked = float(input("How many hours did you work? "))
    
    gross_pay = hourly_wage * hours_worked
    federal_tax = gross_pay * 0.10
    state_tax = gross_pay * 0.05
    social_security = gross_pay * 0.062
    net_pay = gross_pay - (federal_tax + state_tax + social_security)
    
    print(f"\nGross Pay: ${gross_pay:.2f} ({hours_worked} hours @ ${hourly_wage:.2f}/hr)")
    print(f"Federal tax: ${federal_tax:.2f}")
    print(f"State tax: ${state_tax:.2f}")
    print(f"Social security: ${social_security:.2f}")
    print(f"Net pay: ${net_pay:.2f}\n")

def revenue_or_expense(revenue_expenses):
    while True:
        transaction_name = input("Enter transaction name: ")
        transaction_type = input("Is this a revenue or an expense? (R/E): ").strip().upper()
        amount = float(input("Enter amount: "))
        
        if transaction_type == 'E':
            amount = -abs(amount)
        else:
            amount = abs(amount) 
        
        revenue_expenses.append((transaction_name, amount))
        
        another = input("Another? (Y/N): ").strip().upper()
        if another != 'Y':
            break

def calculate_discretionary(revenue_expenses):
    total_revenue = sum(amount for _, amount in revenue_expenses if amount > 0)
    total_expenses = sum(amount for _, amount in revenue_expenses if amount < 0)
    discretionary_income = total_revenue + total_expenses
    return discretionary_income

def menu():
    print("\nWelcome to My Finance!")
    print("1-Calculate net pay")
    print("2-Enter revenue or expense")
    print("3-Show discretionary income")
    print("4-Exit")
    
    while True:
        choice = input("Choice: ")
        if choice.isdigit() and 1 <= int(choice) <= 4:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def main():
    revenue_expenses = []

    while True:
        user_choice = menu()
        
        if user_choice == 1:
            calculate_net_pay()
        elif user_choice == 2:
            revenue_or_expense(revenue_expenses)
        elif user_choice == 3:
            discretionary_income = calculate_discretionary(revenue_expenses)
            print(f"Revenue: ${sum(amount for _, amount in revenue_expenses if amount > 0):.2f}")
            print(f"Expenses: ${-sum(amount for _, amount in revenue_expenses if amount < 0):.2f}")
            print(f"Discretionary: ${discretionary_income:.2f}")
        elif user_choice == 4:
            print("Thank you for using My Finance!")
            break

if __name__ == "__main__":
    main()

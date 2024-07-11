def  revenue_or_expense():
    while True:
        transaction_name = input("Enter transaction name: ")
        transaction_type = input("Is this a revenue or an expense? (R/E): ").strip().upper()
        amount = float(input("Enter amount: "))

        if transaction_type =='E':
            amount = -abs(amount)
        else:
            amount =abs(amount)

            revenue_expenses.append((transaction_name, amount))
        
        another = input("Another? (Y/N): ").strip().upper()
        if another != 'Y':
            break
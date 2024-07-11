def main():
    while True:
        print("\nMenu:")
        print("1 - Calculate net pay")
        print("2 - Enter revenue or expense")
        print("3 - Show discretionary income")
        print("4 - Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            calculate_net_pay()
        elif choice == '2':
            revenue_or_expense()
        elif choice == '3':
            show_discretionary_income()
        elif choice == '4':
            print("Thanks for using My Finance!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

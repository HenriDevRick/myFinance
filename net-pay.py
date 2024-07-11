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
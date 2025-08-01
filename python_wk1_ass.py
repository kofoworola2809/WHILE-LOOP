print("👋 Welcome to the Simple Calculator!")

while True:
    try:
        first_number = int(input("\nEnter the first number: "))
        second_number = int(input("Enter the second number: "))
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")
        continue

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter choice (1–4): "))
    except ValueError:
        print("❌ Invalid input! Please enter a number between 1 and 4.")
        continue

    print("\n...........Result..........:")

    if choice == 1:
        print(f"Sum: {first_number + second_number}")
    elif choice == 2:
        print(f"Difference: {first_number - second_number}")
    elif choice == 3:
        print(f"Product: {first_number * second_number}")
    elif choice == 4:
        if second_number == 0:
            print("❌ Cannot divide by zero!")
        else:
            print(f"Quotient: {first_number / second_number}")
    else:
        print("❌ Invalid choice. Please select a number between 1 and 4.")
        continue

    # Ask user to continue using number options
    print("\nDo you want to perform another calculation?")
    print("1. Yes")
    print("2. No")
    
    try:
        continue_choice = int(input("Enter your choice (1 or 2): "))
    except ValueError:
        print("❌ Invalid input! Exiting for safety.")
        break

    if continue_choice != 1:
        print("\n👋 Thank you for using the calculator!")
        break


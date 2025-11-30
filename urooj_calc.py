#making function for operations
def urooj_calc():
    
    while True:
        print("\nSelect Option:")
        print("1. Calculations")
        print("2. Exit")
        choice = input("Enter choice: ")

        if choice == "2":
            print("Exiting")
            break

        elif choice =="1":
            a = float(input("\nEnter first number : "))
            b = float(input("Enter second number: "))
            print ("\nAddition:    ", a + b)
            print ("Subtraction:  ",round( a - b))
            print ("Product:   ", a * b)
            print ("Division:   ", round(a / b,2) if b != 0 else "Division by zero is not possible try another number")
 
        else:
            print("Invalid choice")
#calling function

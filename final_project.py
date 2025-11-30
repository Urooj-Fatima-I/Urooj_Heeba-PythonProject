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
import random

def heeba_number_game():
 print("NUMBER GUESSING GAME!")
 print("Try guessing the number in the range 1-50")
 while True:
    secret_number = random.randint(1, 50)
    attempts = 0
    while True:
        guess = int(input("Enter a number: "))
        attempts += 1

        if guess == secret_number:
            print("Congratulations! You have guessed the secret number.")
            break
        elif guess > secret_number:
            print("Your guess is too high!")
        else:
            print("Your guess is too low!")

    print(f"The secret number is {secret_number}")
    print(f"Total attempts: {attempts}")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != "yes":
        print("Thank you for playing champ!")
        break


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

heeba_number_game()
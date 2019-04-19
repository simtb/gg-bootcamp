import random

if __name__ == "__main__":
    number_of_guesses = 1
    random_number = random.randint(0, 100)

    print("Enter a value")
    user_guessed_number = int(input())

    while user_guessed_number != random_number:
        if user_guessed_number < random_number:
            print("Unlucky! The number I'm thinking off is greater")
            print("Try again... please enter a number:")
            user_guessed_number = int(input())
            number_of_guesses += 1
        else:
            print("Unlucky! The number I'm thinking off is smaller")
            print("Try again... please enter a number:")
            user_guessed_number = int(input())
            number_of_guesses += 1

    print(f"Congrats! You guessed right in {number_of_guesses} guesses, the number I am thinking off is {random_number}")
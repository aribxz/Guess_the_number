import random

a = random.randint(1, 100)
def game():
    print("Welcome to the Guess the Number game!")
    print("Try to guess the number I'm thinking of between 1 and 100.")
    
    score = 0
    attempts = 0
    
    while True:
        guess = input("Enter your guess (or type 'exit' to quit): ")
        
        if guess.lower() == 'exit':
            print("Thanks for playing! Your final score is:", score)
            break
        
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess < a:
            print("Too low! Try again.")

        elif guess > a:
            print("Too high! Try again.")

        else:
            score = max(100 - attempts * 10, 0)  # Calculate score based on attempts
            print(f"Congratulations! You've guessed the number {a} in {attempts} attempts.")
            print(f"Your score is: {score}")
            break

game()        
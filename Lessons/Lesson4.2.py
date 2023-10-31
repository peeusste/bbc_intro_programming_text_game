# Lessson4.2.py
# Create a number guessing game! 
# The user has a pre-defined number of tries to guess a number between 1 and 10
# Give the user relevant messaging whilst attempting to guess the number
# HINT: You may need to use the break command to exit the loop

import random # bring the prewritten random code into our code

# User has to guess a random number with num_guesses set to 3
to_guess = random.randint(1, 10)
num_guesses = 3 

print("The Number Guessing Game. You have", num_guesses, "tries")
print("=================================================")
while num_guesses>0:
    guess = int(input("Guess a number between 1 and 10>"))
    if guess == to_guess:
        print("Congratulations! You guessed the number!")
        break
    else: 
        num_guesses -= 1
        if num_guesses > 0:
            print("Sorry, that's wrong. You have", num_guesses, "left")
        else:
            print("You are out of tries! The number was", to_guess)

  

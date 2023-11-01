# Practical exercise
# Set a predefined password
# Prompt the user to enter a password 
# If they enter the wrong password display an error message. If it's correct then display a success message

# Predefined password
password = "welovepython"
user_input = input("Enter the password: ")

# Check if the entered password matches the predefined password
if user_input == password:
    print("Success! You've entered the correct password.")
    
if user_input != password:
    print("Incorrect! You've entered the wrong password.")

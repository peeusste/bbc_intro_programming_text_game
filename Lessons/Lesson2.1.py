# Practical exercise

# Create a countdown timer that counts down from a specified number entered by the user until it reaches zero
# Use appropriate messaging, like at a rocket launching!

# Prompt the user for a starting number
start_number = int(input("Enter a number to start the countdown: "))
print("Let the countdown commence!")
# Use a while loop to count down to zero
while start_number > 0:
    print(start_number)
    start_number -= 1

# Print the final message after the loop
print("We have lift off!")

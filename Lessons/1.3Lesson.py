# Practical exercise
# Prompt the user to enter  their favourite pizza and favourite topping
# Print a personalised message eg saying it's a good choice and it's your favourite

# Prompt the user for their favourite pizza
pizza = input("What's your favourite pizza? ")

# Prompt the user for their favourite topping
topping = input("And what's your favourite pizza topping? ")

# Print the personalized greeting
print("Great choice!", pizza, "with", topping, "is my favourite too!")

# Extra challenge
# A pizza restaurant lets you build your own pizza.



# Ask the user for the base price of a pizza
pizza_price = float(input('What is the base price of the pizza? £'))

# Ask how many extra toppings they want
number_of_toppings = int(input('How many extra toppings would you like? '))

# Each topping costs £1.50
# Could have a variable topping_cost = 1.50 or hard-code into the final_price as below

# Calculate and print the final price

final_price = pizza_price + (number_of_toppings * 1.50)

print('The final price is £', final_price)

# Crazy Fruits Coding Challenge
# Your friend has a number of fruits in a bag and asks you to count the number of bananas and apples
# First, ask her how many she has
# Then as she takes each one out of the bag, ask her to enter the type of fruit (banana, apple etc)
# Count the number of bananas and apples as you go along until there are no more fruits left 
# Finally, print out the total number of bananas and apples
# Tip: When testing, start off with a small number of fruits to begin with

# You can solve this challenge by using inputs, variables for counters, a while loop and if/elif statements

fruit_count = int(input("How many fruits do you have?"))
banana_count = 0
apple_count = 0

i = 0
while i < fruit_count:
    fruit = input("What piece of fruit did you take out of the bag?")
    if fruit == "banana":
        banana_count = banana_count + 1
    elif fruit == "apple":
        apple_count = apple_count + 1
    i = i + 1

print("You have", banana_count, "bananas")
print("You have", apple_count, "apples")    

# Extra crazy challenge
# Oh oh, your friend has just said to you that she now wants to know how many other items were in the bag! 
# Add a catch-all for other items and print out the number of other items.

fruit_count = int(input("How many fruits do you have?"))
banana_count = 0
apple_count = 0
other_count = 0

i = 0
while i < fruit_count:
    fruit = input("What piece of fruit did you take out of the bag?")
    if fruit == "banana":
        banana_count = banana_count + 1
    elif fruit == "apple":
        apple_count = apple_count + 1
    else:
        other_count = other_count + 1
    i = i + 1

print("You have", banana_count, "bananas")
print("You have", apple_count, "apples")
print("You also have", other_count, "other items")    

# Challenge #1
# Create a list of favourite films 
# Print out the films with an appropriate message
# The films could be  "Citizen Kane", "The Matrix", "The Godfather" and "The Shawshank Redemption"


films = ["Citizen Kane", "The Matrix", "The Godfather", "The Shawshank Redemption"]

# Counter to run through list
i = 0

# Loop through and print each film 
while i < len(films):
    print(films[i], "is one of your favourite films")    
    i += 1

# Challenge #2
# Using the same list of films, prompt the user with the name of the film and ask for a rating for that film
# Print out the films and their corresponding ratings
# HINT: Create an empty list to store the ratings in 

films = ["Citizen Kane", "The Matrix", "The Godfather", "The Shawshank Redemption"]

# Empty list to store ratings
ratings = []

# Counter to run through list
i = 0

# Loop through each film and prompt the user for a rating
while i < len(films):
    print(films[i])    
    rating = int(input("Rate this film (1-5):"))
    ratings.append(rating)
    i += 1

# Print out the films and their corresponding ratings
print("Your film ratings are:")

# Counter to run through list
i = 0
while i < len(films):
    print(films[i], "-", ratings[i])
    i += 1



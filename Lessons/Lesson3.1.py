# From a predefined list of films prompt the user with the name of each film and get a rating for the films
# Print out the films and their corresponding ratings
# The films are "Citizen Kane", "The Matrix", "The Godfather" and "The Shawshank Redemption"
# HINT: Create an empty list to store the ratings in 

films = ["Citizen Kane", "The Matrix", "The Godfather", "The Shawshank Redemption"]

# Empty list to store ratings
ratings = []

# Counter to run through list
i=0

# Loop through each film and prompt the user for a rating
while i<len(films):
    film=films[i]
    print(film)    
    rating = int(input("Rate this film:"))
    ratings.append(rating)
    i+=1

# Print out the films and their corresponding ratings
print("Your film ratings are:")

# Counter to run through list
i=0
while i<len(films):
    print(films[i], "-", ratings[i])
    i+=1

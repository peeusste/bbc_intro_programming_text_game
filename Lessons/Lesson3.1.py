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

# Extra exercise (no code needed)

# How would you work out what the favourite film was? 
# Set max_rating to 0. Loop over the ratings and if the rating is greater than the current max_rating then that's the new max_rating
# Can you see any issues and how would you resolve this?
# If there are multiple films with the same score only one film would be stored. 
# You could create a list of fave_films and if the score is equal to the max rating then append this to the list. If the rating is greater then set the list to be just this one film

max_fave=ratings[0]
faves=[]
faves.append(films[0])
i=1
while i<len(films):
    if ratings[i]>max_fave:
        max_fave=ratings[i]
        faves=films[i]
    elif ratings[i]==max_fave:
        faves.append(films[i])
    i+=1
    
print(faves, "with a rating of", max_fave) 

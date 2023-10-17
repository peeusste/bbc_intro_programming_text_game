# Extra exercise (no code needed)
## Practical exercise
# Following on from the previous exercise about films...
# Display what the favourite film was (ie the one with the highest rating) and its rating
# Can you see any issues and how would you resolve this?
# Need to resolve the scenario where  two films have the same rating

# Set max_rating to 0. Loop over the ratings and if the rating is greater than the current max_rating then that's the new max_rating
# If there are multiple films with the same score only one film would be stored. 
# Create a list of fave_films and if the score is equal to the max rating then append this to the list. If the rating is greater then set the list to be just this one film

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
if len(faves)==1:
    print("Your favourite film is",faves[0], "with a rating of",max_fave)
elif len(faves)>1:
    print"You had more that one favourite film with a rating of", max_fave,"These were:")
    i=0;
    while i<len(faves):
        print(faves[i])
        i+=1
        

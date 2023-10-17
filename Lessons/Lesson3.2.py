# Extra exercise (no code needed)
## Practical exercise
# Following on from the previous exercise about films...
# Display what the favourite film was (ie the one with the highest rating) and its rating
# Can you see any issues and how would you resolve this?
# Need to resolve the scenario where  two films have the same rating

films = ["Citizen Kane", "The Matrix", "The Godfather", "The Shawshank Redemption"]

# Empty list to store ratings
ratings = []

# Counter to run through list
i=0

# Loop through each film and prompt the user for a rating
while i<len(films):
    print(films[i])    
    rating = int(input("Rate this film:"))
    ratings.append(rating)
    i+=1

# faves list to store the faves!
faves=[]
# Assume the first film is the fave
faves.append(films[0])
max_fave=ratings[0]

i=1
# Loop over the films and find the fave (or faves)
while i<len(films):
    if ratings[i]>max_fave:
        max_fave=ratings[i]
        # reset the faves list
        faves=[]
        faves.append(films[i])
    elif ratings[i]==max_fave:
        faves.append(films[i])
    i+=1
if len(faves)==1:
    print("Your favourite film is",faves[0], "with a rating of",max_fave)
elif len(faves)>1:
    print("You had more that one favourite film with a rating of", max_fave,"These were:")
    i=0;
    while i<len(faves):
        print(faves[i])
        i+=1
        

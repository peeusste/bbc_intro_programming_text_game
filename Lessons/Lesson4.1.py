# Create a dictionary for a book that contains key-value pairs for title, author, published_year and genre
# Create variables for each that stores each value and print out a meaningful phrase using the variables 
# Change one or more of the values and print out the new phrase

book = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "published_year": 1960,
    "genre": "Novel"
}

# Assigning values to variables
title = book["title"]
author = book["author"]
published_year = book["published_year"]
genre = book["genre"]

print(title, "is a", genre, "written by", author, "and was published in", published_year)

book["published_year"]=1961
published_year = book["published_year"]
print(title, "is a", genre, "written by", author, "and was published in", published_year)

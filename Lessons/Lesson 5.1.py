# Lesson 5.1
# Create your own dictionary of dictionaries
# Create a similar structure to the one above but personalise it 
# It could be your friends and family, or characters in your favourite Netflix series
# Print some of the details to the screen

friends = {
    'dave': {
        'name': 'Dave',
        'placeOfBirth': 'Birmingham',
        'skill': 'Plays guitar',
        'number_of_languages_spoken': 1
    },
    'andrea': {
        'name': 'Andrea',
        'placeOfBirth': 'Aberdeen',
        'skill': 'Carpentry',
        'number_of_languages_spoken': 2
    },
    'chris': {
        'name': 'Chris',
        'placeOfBirth': 'Devon',
        'skill': 'Great organiser',
        'number_of_languages_spoken': 1
    }    
}

# print (friends)
print ("My friend",friends['andrea']['name'], "has a special skill. It is", friends['andrea']['skill'],)
print ("She was born in", friends['andrea']['placeOfBirth'])

# Lesson6.1.py
# You've intercepted a secret message that's been passed from one of the delegates on the course to another
# It is gobbledegook but you've also discovered the cypher!
# Subsitutions have been made with:
#   a space being replaced by #
#   L with ! 
#   i with £
#   e with $
#   a with %
#   o with ^
#   t with &
# Decrypt the secret message and split it into words using ONE LINE of Python
# Print out the full decryted message and how many words are in the message
# Do the reverse and encrypt the message to check it works
# Finally accept some user input and encrypt that message

secret_message='H$ll^,#&h£s#£s#%#gr$%&#py&h^n#c^urs$#%nd#I#%m#l$%rn£ng#%#l^&'

decoded_message = (secret_message.replace('#', ' ')
                                    .replace('!', 'L')
                                    .replace('£', 'i')
                                    .replace('$', 'e')
                                    .replace('%', 'a')                                    
                                    .replace('^', 'o')
                                    .replace('&', 't')
                                     )
                                    
translated_message = decoded_message.replace(' ', '#').replace('L', '!').replace('i', '£').replace('a', '%').replace('e', '$').replace('o', '^').replace('t', '&')

if translated_message==secret_message: 
    print ("We have a match, so  the code works!")

print(decoded_message)


# message was "Hello, this is a great python course and I am learning a lot"

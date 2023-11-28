# Initial names and roles data

roles = {
    "Alicia": "Software Engineer", 
    "Sven": "Designer", 
    "Charlie": "Manager", 
    "Rani": "Business Analyst"
    }

# User input
name = input("Enter a name to find their role: ")

if name in roles:
    print(name,"is a", roles[name])
else:
    print("Name not found, sorry!")

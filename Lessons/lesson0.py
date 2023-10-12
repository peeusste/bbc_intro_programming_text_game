#This is a comment. Comments are just any text preceded by the # symbol

#The following line will print out the Hello, World phrase to the console
print("Hello, World!")

#Python is very fussy about indentation
print("Hello, World!")

#Indented line
  print("Hello, World Again!") # This will  give an error as it's not on the same (code block) level as the the first statement

#Variables are used to store values
x = 23         # x is the number 23
y = 4          # y is the number 4
f = "banana"   # f is the string "banana"

#Where desirable it's good practice to use descriptive variable names
fruit = "banana"

#You can output variables as you would expect
print(x)
print(y)
print(fruit)

#And you can combine then with other strings
print("My favourite fruit is", fruit)

#Many operations can be done on variables too
z=x+y
print(z)

#Or better
print(x, "+", y, "=", z)

#EXERCISE
# Create two variables for two people's name and two for their age. Print out their names, ages and combined age

person1 = "Sam"
agePerson1 = 23
person2 = "Suri"
agePerson2 = 35

print(person1, "is", agePerson1) 
print(person2, "is", agePerson2) 
print("Their combined age is", agePerson1 + agePerson2)

''' 
#Could also do
combinedAge = agePerson1 + agePerson2
print("Their combined age is", combinedAge)
'''




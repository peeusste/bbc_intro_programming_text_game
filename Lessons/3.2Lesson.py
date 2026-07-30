# Ask the user for a temperature
temperature = int(input('Enter a temperature > '))

# Use the or keyword to decide whether the temperature is extreme
# You can choose your own definition of an extreme temperature
if temperature < 0 or temperature > 30:
    print('Extreme temperature, take care if you are going outside.')
else:
    print('Normal temperature, enjoy your day!')

# Ask the user about the weather and their preference
good_weather = input("Is the weather good today? (yes/no): ")
prefers_outdoor = input("Do you prefer outdoor activities? (yes/no): ")

# Suggest an outing based on the user's answers
if good_weather=="yes" or prefers_outdoor=="yes":
    print("How about a walk in the park?")
else:
    print("Maybe visit a cafe or a library today.")

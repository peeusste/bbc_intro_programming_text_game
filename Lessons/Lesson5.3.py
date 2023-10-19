# Lesson 5.3

# Take the famous quote: "The course of true love never did run smooth"
# Split the quote at every space to get individual words
# Print out the list of words
# Count and print the number of words in the quote
# Print out the first word and the last word

quote = 'The course of true love never did run smooth'


quote_list = quote.split(' ') # Split the text that is separated by spaces into a mylist 


print("Words:", quote_list)

len=len(quote_list)

# Print the number of words and the first/last word
print("Number of Words:", len)
print ('The first word is ',quote_list[0], 'and the last word is', quote_list[len-1])



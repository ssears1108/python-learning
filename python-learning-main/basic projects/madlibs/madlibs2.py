import random

string1="This is a string"
string2=string1.replace("is","was")
print(string2)

#below reads a file and replaces a word with user input
# Open the Mad Libs text file
f = open('madtext.txt','r')
 
# Read the whole file and store each line in a list
madlibText = f.readlines()
 
# Choose a random line from the list
madlib = random.choice(madlibText)

#prints the randomly choosen line for the user to see
print(madlib)
 
# Ask the user to input a noun
noun = input("Enter a noun: ")
 
# Replace the blank with the user's input
madlib = madlib.replace("blank", noun)
 
# Print out the Mad Lib including the user's response
print(madlib)
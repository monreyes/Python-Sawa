# This program says hello and asks for my name

print('Hello World')
# print('What is your name?') # ask for the name
myName = raw_input('What is your name?')
print("It's good to meet you, " + myName)
print('The length of your name is :' + str(len(myName))+ ' letters')
myAge = raw_input('How old are you?')
print('You will be '+ str(int(myAge)+1) + ' in a year')

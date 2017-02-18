#Guess the number I am thinking in 5 tries
import random
guesses = 0
minnum = 1
maxnum = 100
tries = 5

print("Hi there, welcome to my world")
yourName = raw_input("What is your name?")

mynum = random.randint(1,100)
#print mynum


print('Nice to meet you '+ yourName +' ,well I am thinking of a number from ' + str(minnum) +' to '+ str(maxnum) )
#print(minnum  maxnum)
#yourguess = print("Guess my number: ")

while guesses < tries:
    print('Guess my number.')
    guess = input()
    guess = int(guess)

    guesses = guesses + 1

    if (guess < minnum or guess > maxnum):
        print('Pay attention! I told you, the number is between '+ str(minnum) +' and '+ str(maxnum) +' only!')

    if guess < mynum:
        print('Your guess is too low. You only have '+ str(tries - guesses) +' tries left')

    if guess > mynum:
        print('Your guess is too high.You only have '+ str(tries - guesses) +' tries left')

    if guess == mynum:
        break

if guess == mynum:
    guesses = str(guesses)
    print('Good job ! How did you do that? You guessed my number in ' + guesses + ' guesses!')

if guess != mynum:
    mynum = str(mynum)
    print('Sorry, not the right number.It was ' + mynum)

from random import randint

def promptforquestion():
    question = input("What is your question? ")
    return question

promptforquestion()

answer = randint(1, 15)

if (answer == 1):
    print ("Yes.")

elif (answer == 2):
    print ("It is certain.")

elif (answer == 3):
    print ("It is decidedly so.")

elif (answer == 4):
    print ("Yes definitely.")

elif (answer == 5):
    print ("Most likely.")

elif (answer == 6):
    print ("Reply hazy, try again.")

elif (answer == 7):
    print ("Ask again later.")

elif (answer == 8):
    print ("Better not tell you now.")

elif (answer == 9):
    print ("Cannot predict now.")

elif (answer == 10):
    print("Concentrate and ask again.")

elif (answer == 11):
    print("No.")

elif (answer == 12):
    print("Don't count on it.")

elif (answer == 13):
    print("Outlook not so good.")

elif (answer == 14):
    print("Very doubtful.")

elif (answer == 15):
    print("Not likely.")

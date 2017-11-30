import random

print('--------------------------------------')
print('         Guess That Number Game       ')
print('--------------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

name = input('Player what is your name?')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print("{0}... That guess of {1} is too Low".format(name, guess))
    elif guess > the_number:
        print("{0}... That guess of {1} is too High".format(name, guess))
    else:
        print('{0} you win!'.format(name))

print("All Done")
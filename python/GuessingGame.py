import random

number = random.randint(0,100)
guess = 0

while guess != number:
    try:
       guess = int(input("Guess a number between 0 and 100: "))
       if guess < number:
           print("fuck man that's Too low")
       elif guess > number:
           print("fuck man , that's Too high")
       else:
           print("Oh shit You got it!")
        
    except ValueError:
        print("Please enter a number")
       
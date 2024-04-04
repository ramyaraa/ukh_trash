name1 = input("what is your name? ") 
name2 = input("what is you name of love friend? ") 

both = name1 + name2
bothlo = both.lower()
t = bothlo.count("t")
r = bothlo.count("r")
u = bothlo.count("u")
e = bothlo.count("e")
firstDigit = t + r + u + e
l = bothlo.count("l")
o = bothlo.count("o")
v = bothlo.count("v")
e = bothlo.count("e")
secondDigit = l + o + v + e
score = int(str(firstDigit) + str(secondDigit))
if score <= 10 or score >= 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
# This is a simple project designed to test a password a user inputs and grades it from 0 to 10.
# Inspireed by NeuralNine's Password Strength Checker Tutorial ----> https://www.youtube.com/watch?v=iJ01q-sRJAw

import string
password = "helloworld"
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
special = any([1 if c in string.ascii_uppercase else 0 for c in password])
digits = any([1 if c in string.ascii_uppercase else 0 for c in password])

characters = [upper_case, lower_case, special, digits]
length = len(password)

score = 0


if length > 8:
    score += 1
elif length > 12:
    score += 1
elif length > 17:
  score += 1
if length > 20:
  score += 1


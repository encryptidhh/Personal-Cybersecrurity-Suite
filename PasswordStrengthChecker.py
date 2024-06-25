# This is a simple project designed to test a password a user inputs and grades it from 0 to 7.
# Inspired by NeuralNine's Password Strength Checker Tutorial ----> https://www.youtube.com/watch?v=iJ01q-sRJAw

import string
import itertools
import time

charset = string.ascii_letters + string.digits + string.punctuation

# User-prompted password input & calculating the strength of the user's password
password = input("Enter your password: ")
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]
length = len(password)

# Function to perform brute-force attack
def brute_force_crack(target):
    start_time = time.time()
    attempts = 0
    # Generate combinations of increasing length
    for password_length in range(1, len(target) + 1):
        for guess in itertools.product(charset, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == target:
                end_time = time.time()
                return attempts, end_time - start_time
    return None, None # The function returns "None" if password is not found

# Code that calls the brute_force_crack function
attempts, time = brute_force_crack(password)
if attempts is not None:
    print("Brute-force attempts:", attempts)
    print("Time to crack:", time)
else:
    print("Password not found in brute-force attack.")
    exit()

# "score" variable initialization and checking if password is found in a common list
score = 0
with open("commonpasswords.txt", "r") as f:
    common = f.read().splitlines()
    if password in common:
        print("Password was found in a common list. Score: 0/7")
        exit()

# More password scoring
if length > 8:
    score += 1
elif length > 12:
    score += 1
elif length > 17:
    score += 1
if length > 20:
    score += 1

# Messages for each grade the password gets
if score == 7:
    print("Password is very strong. Score: 7/7")
elif score == 6:
    print("Password is very strong. Score: 6/7")
elif score == 5:
    print("Password is strong. Score: 5/7")
elif score == 4:
    print("Password is moderate. Score: 4/7")
elif score == 3:
    print("Password is alright. Score: 3/7")
elif score == 2:
    print("Password is weak. Score: 2/7")
elif score == 1:
    print("Password is very weak. Score: 1/7")
else:
    print("Password is very weak. Score: 0/7")

# Display attempts and time to crack
attempts, time = brute_force_crack(password)
print("Brute-force attempts: " + str(attempts))
print("Time to crack: " + str(time))

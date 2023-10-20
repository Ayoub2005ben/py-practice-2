'''
Exercises for random
'''

import random

# 1. Write some code that prints the numbers from 1 to 10 and stores them in a list called numbers.
numbers = list(range(1,11))
print(numbers)

# 2. Shuffle the list and print it out.
random.shuffle(numbers)
print(numbers)
import random

numbers = list(range(1, 11))
random.shuffle(numbers)
print(numbers)




# 3. Choose a random number from the list and print it out.
random_number = random.choice(numbers)
print(f"Random number from the list: {random_number}")
list(range(1, 11))
random.shuffle(numbers)
random_number = random.choice(numbers)
print(f"Random number from the list: {random_number}")

# 4. Choose a random number from 1 to 100 and print it out.
random_number = 0 # fix this
print(f"Random number between 1 and 100: {random_number}")
import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Print the random number
print(f"Random number from 1 to 100: {random_number}")


# 5. Sample 5 numbers uniques from numbers list and print them out.
random_samples = [] # fix this
print("Random samples:", random_samples)
import random

# Assuming you have a list called 'numbers'
numbers = list(range(1, 101))  # Adjust the range as needed

# Sample 5 unique numbers from the list
sampled_numbers = random.sample(numbers, 5)

# Print the sampled numbers
print("Sampled unique numbers:", sampled_numbers)


# 6. Create a list of days of the week in a variable days and print a random day of the week.
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
random_day = "" # fix this
print("Random day of the week:", random_day)
import random

# Create a list of days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Choose a random day from the list
random_day = random.choice(days)

# Print the random day of the week
print(f"Random day of the week: {random_day}")



# 7. Dice roll simulator: print a random number from 1 to 6.
dice_roll = 0 # fix this
print("Dice roll:", dice_roll)
import random

# Simulate a dice roll
dice_roll = random.randint(1, 6)

# Print the result
print(f"The dice rolled: {dice_roll}")


# 8. Coin flip: randomly chooses "heads" or "tails".
coins = ['heads','tails']
coin = "" # fix this
print("Coin flip:", coin)
import random

# Create a list with "heads" and "tails"
coin_sides = ["heads", "tails"]

# Use random.choice() to randomly select one of the sides
result = random.choice(coin_sides)

# Print the result of the coin flip
print(f"The coin landed on: {result}")


# 9. Ask the user for a number and print out a random number from 1 to the number the user chooses.
# hint: use int(input("..."))
user_number = 0 # fix this
random_number = 0 # fix this, random number from 1 to user_number
print(f"Random number from 1 to {user_number}: {random_number}")
import random

# Ask the user for a number
user_number = int(input("Enter a number: "))

# Generate a random number from 1 to the user's number
random_number = random.randint(1, user_number)

# Print the random number
print(f"Random number from 1 to {user_number}: {random_number}")



# 10. Ask the user to guess a number from 1 to 10 and tell them whether they guessed correctly or not.
user_guess = 0 # fix this, hint: use int(input("..."))
random_number = 10 # fix this, random number from 1 to 10
if user_guess == random_number:
  print("You guessed correctly!")
else:
  print("You guessed incorrectly.")
  import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Ask the user to guess
user_guess = int(input("Guess a number from 1 to 10: "))

# Check if the user's guess is correct
if user_guess == random_number:
    print(f"Congratulations! You guessed correctly. The number was {random_number}.")
else:
    print(f"Sorry, you guessed incorrectly. The correct number was {random_number}.")



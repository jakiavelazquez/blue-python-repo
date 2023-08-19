import random

number = random.randint(0, 100)  # Generates a random number between 0 and 100
counter = 0

while number != 52:  # Executes the loop as long as the number is not equal to 52
    number = random.randint(0, 100)  # Generates a new random number
    counter = counter + 1  # Increments the counter by 1

print(counter, number)  # Prints the final counter and the number

############################

for i in range(10):  # Iterates over the range from 0 to 9
    print(i * 2)  # Prints the value of i multiplied by 2

############################

number = random.randint(0, 100)  # Generates a random number between 0 and 100

for i in range(1000):  # Iterates 1000 times
    print(number)  # Prints the current value of number
    if(number == 52):  # Checks if the number is equal to 52
        break  # Exits the loop if the condition is true
    else:
        number = random.randint(0, 100)  # Generates a new random number if the condition is false

print(i, number)  # Prints the final counter and the number

##############################

counter = 0

while counter < 10:  # Executes the loop as long as the counter is less than 10
    print(counter * 2)  # Prints the value of counter multiplied by 2
    counter = counter + 1  # Increments the counter by 1

##############################

number = random.randint(0, 20)  # Generates a random number between 0 and 20

for i in range(number):  # Iterates the number of times specified by the random number
    print('here')  # Prints the string 'here'

##############################

number = random.randint(0, 20)  # Generates a random number between 0 and 20
counter = 0

while number < 20:  # Executes the loop as long as the number is less than 20
    print('here')  # Prints the string 'here'
    number = number + 1  # Increments the number by 1
    counter = counter + 1  # Increments the counter by 1

print(counter, number)  # Prints the final counter and the number

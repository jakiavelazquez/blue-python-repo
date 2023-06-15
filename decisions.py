import random

number = random.randint(0, 10)

if number > 7:
    print('big number')
elif number < 7:
    print('small number')
elif number == 7:
    print('number equals 7')

if number > 4:
    print('number is greater than 4')
print(number)
counter = 1
while counter <11:
    print (counter)
    counter +=1
print('Finished!')

secret_number = 14
print('''
    ==========================
    === SECRET NUMBER GAME ===
    ==========================
    ''')
user_input = int(input('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
    print('Wrong!')
    user_input = int(input('Try to guess the secret number from 1 to 20: '))
print('Perfect! You have guessed the secret number!')
# available logical operators
#
# < less than
# > greater than
# <= less than or equal
# >= greater than or equal
# == equals
# != not equals
password = input('Do you know the secret password? ')
if password != '--secret':
    print('not correct')
else:
    print('correct password')
if True:
    print('Condition met')
if False:
    print('Condition met')
if 2 == 2:
    print('true')
if 1 == 2:
    print('true')
if 2 == 2.0:
    print('true')
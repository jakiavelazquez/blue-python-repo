#factorial
# 3! = 1 * 2 * 3 = 6
# 5% = 1 * 2 * 3 * 4 * 5 = 120

#interative
def get_factorial(number):
    factorial = 1
    for x in range(1, number +1):
        factorial *= x
    return factorial

print(get_factorial(6))

def get_factorial_recursive(number):
    if number <= 1:
        return 1
    return number * get_factorial_recursive(number - 1)

print(get_factorial_recursive(6))
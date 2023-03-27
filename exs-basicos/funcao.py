def multi(*args):
    numbers = args
    total = 1
    for number in numbers:
        total *= number
    return total


def define(number):
    if number % 2 == 0:
        return f'Número par'
   
    else:
        return f'Número ímpar'
    
print(multi(3, 3, 3 ))
print(define(2))
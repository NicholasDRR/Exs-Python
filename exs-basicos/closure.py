def primary(number):
    def secondary(opt):
        if opt == 2:
            return f'{number} x {opt} = {number * 2}'
        if opt == 3:
            return f'{number} x {opt} = {number * 3}'
        if opt == 4:
            return f'{number} x {opt} = {number * 4}'

    return secondary

multiply = primary(2)

print(multiply(2))
print(multiply(3))
print(multiply(4))
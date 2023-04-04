#generator = (c for c in range(1000000))
#
#for value in generator:
#    print(value)

def generator(n=0, max=0):
    while True:
        yield n
        n +=1
        if n > max:
            return 'stop'
        
gen = generator(max=10)

#for values in gen:
#    print(values)

def gen2():
    yield from generator()
    yield 2
    yield 3
    yield 4
    
gene2 = gen2()

for values in gene2:
    print(values)
    
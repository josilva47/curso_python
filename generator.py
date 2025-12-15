
''''
Generators são funções (ou expressões) que:

- produzem valores sob demanda

- usam yield em vez de return

- não guardam tudo na memória

- lembram onde pararam entre uma execução e outra
'''

def generator():
    yield 1 #pausa
    print('Continuando')
    yield 2 #pausa
    print('Continuando')
    yield 3
    

gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))


#Herdando de outro generator

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6

print()
g = gen2()

for n in g:
    print(n)

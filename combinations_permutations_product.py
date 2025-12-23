#Combinations - é uma função do módulo itertools usada para gerar todas as combinações possíveis de elementos de um iterável, sem repetição e sem considerar a ordem.

#Permutations - é uma função do módulo itertools que gera todas as permutações possíveis de um iterável. Aqui a ordem importa e sem repetição

#é uma função do módulo itertools que gera o produto cartesiano entre iteráveis. Aqui a ordem importa e tem repetição

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas =['Joao', 'Joana', 'Luiz', 'Leticia']

Camisetas = [
    ['Preta', 'Branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino']
]

print_iter(combinations(pessoas, 2)) 
print_iter(permutations(pessoas, 2))
print_iter(product(*Camisetas)) # Passa vários iteráveis Ou usar repeat para repetir o mesmo iterável 
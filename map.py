#map() é uma função embutida do Python que aplica uma função a cada elemento de um iterável (lista, tupla, etc.) e retorna um iterador com os resultados.

def print_iter(iterator):
    print(*iterator, sep='\n')

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]

#SEM UTILIZAR O MAP
novos_produtos = [
    {**p, 'preco':  round(p['preco'] * 1.1, 2)} for p in produtos
]

print_iter(novos_produtos)
print()

#UTILIZANDO O MAP
def muda_preco_produtos(produto):
    return {
        **produto,
        'preco': round(produto['preco'] * 1.1, 2)
    }

novos_produtos_map = map(muda_preco_produtos, produtos) #funcao, iteravel

print_iter(novos_produtos_map)
print()

#OUTRO EXEMPLO
numeros = [1, 2, 3, 4]

#map() não retorna uma lista, retorna um iterador. Por isso, devemos desempacotar ela
#O desempacotamento deve ser feito ja na funçao, pois assim conseguimos consumir ela mais de uma vez
dobro = list(map(lambda x: x * 2, numeros))
print(dobro)
print(dobro)

#Se for desempacotar na saida, so sera possivel consumir uma vez o resultado do map
#print(list(m))    # [1, 2, 3]
#print(list(m))    # []  ❌ acabou
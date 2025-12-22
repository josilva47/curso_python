

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4,]

lista_soma = [
    lista_a[i] + lista_b[i]
    for i in range(len(lista_b))
    ]

print(lista_soma)

#OUTRA MANEIRA

lista_soma = [
    x + y for x, y in zip(lista_a, lista_b) # zip: une as listas até o tamanho da menor lista
    ]

print(lista_soma)
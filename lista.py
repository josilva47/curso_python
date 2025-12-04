"""
Lista é MUTÁVEL
Suporta vários valores de qualquer tipo

--METODOS ÚTEIS--
    append = Adiciona um item ao final
    insert = Adiciona um item no índice escolhido
    pop = Remove do final ou do índice escolhido
    del = Apaga um índice
    clear = Limpa a lista
    extend = Estende a lista

"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) # mexe diretamente na lista A

print(lista_c)
print(lista_a)

#A FORMA DE COPIAR UMA LISTA SIMPLES DA MANEIRA CERTA
original = ['João', 'Araujo']
copia = original[:] # ou com o metodo copy()

print(original)
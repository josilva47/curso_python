import copy
from dados import produtos

print(f"\033[32m{'Ordenados por preço'.center(31)}\033[m")

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos), 
    key=lambda item: item['preco'])

print(*produtos_ordenados_por_preco, sep='\n')

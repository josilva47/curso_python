import copy
from dados import produtos

print(f"\033[32m{'Ordenados por nome'.center(31)}\033[m")

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), 
    key=lambda item: item['nome'], 
    reverse=True)

print(*produtos_ordenados_por_nome, sep='\n')




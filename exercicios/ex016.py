import copy
from dados import produtos

print(f"\033[32m{'Aumento de 10%'.center(31)}\033[m")

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)]

print(*novos_produtos, sep='\n')







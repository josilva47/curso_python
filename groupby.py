#groupby é uma função do módulo itertools que agrupa elementos consecutivos de um iterável com base em uma chave.

from itertools import groupby

alunos = [
    {'Nome': 'Luiz', 'nota': 'A'},
    {'Nome': 'Leticia', 'nota': 'B'},
    {'Nome': 'Fabricio', 'nota': 'A'},
    {'Nome': 'Rosemary', 'nota': 'C'},
    {'Nome': 'Joana', 'nota': 'D'},
    {'Nome': 'Joao', 'nota': 'A'},
    {'Nome': 'Eduardo', 'nota': 'B'},
    {'Nome': 'Andre', 'nota': 'A'},
    {'Nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

ordenado = sorted(alunos, key=ordena)
grupos = groupby(ordenado, key=ordena)

for c, g in grupos:
    print(c)
    for aluno in g:
        print(aluno)
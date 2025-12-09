# Dentro do SET não existe valores duplicados 

"""
---MÉTODOS ÚTEIS---

    add - Adiciona um valor no set
    update - Adiciona um valor iteravel no set
    clear - Limpa os valores do set
    discard - Elimina valores
"""

s1 = set()

s1.add('João')
print(s1)

s1.update('Araujo') # s1.update(('Araujo,')) Não itera
print(s1)

s1.discard('João')
print(s1)

s1.clear()
print(s1)

print()

"""
---OPERADORES ÚTEIS---
| = União de sets
& = Interseção de sets - Itens presentes em ambos
- = Diferença entre sets - Itens presentes apenas no set da esquerda
^ = Diferença simétrica - Itens que não estao em ambos
"""

n1 = {1, 2, 3}
n2 = {2, 3, 4}

uniao = n1 | n2
print(uniao)

ambos = n1 & n2
print(ambos)

presente_na_esquerda = n1 - n2
print(presente_na_esquerda)

nao_ambos = n1 ^ n2
print(nao_ambos)
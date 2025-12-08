'''
    len - Quantas chaves
    keys - Iterável com as chaves
    values - Iterável com os valores
    items - Iterável com chaves e valores
    setdefault - Adiciona valor se a chave não existir 
    copy - retorna uma copia rasa (shallow copy)
    get - Obtém uma chave
    pop - Apaga um item com a chave especificada (del)
    popitem - Apaga o último item adicionado
    update - Atualiza um dicionário com outro
'''

import copy

pessoa = {
    'nome' : 'João Araujo',
    'sobrenome' : 'Santos da Silva'
}

print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.setdefault('idade', 26))

#Faz uma copia profunda, ou seja, essa copia não afeta a original e vice versa
copia = copy.deepcopy(pessoa)

print(pessoa.get('nome'))

print(pessoa.pop('nome'))
print(pessoa) #A chave nome não está mais no dicionario

print(pessoa.popitem())
print(pessoa) #A ultima chave não está mais no dicionario

pessoa.update({
    'idade' : '27',
    'Relacionamento' : 'Solteiro'
})

print(pessoa)


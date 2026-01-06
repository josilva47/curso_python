import json

CAMINHO_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', '26')
p2 = Pessoa('Maria', '30')
p3 = Pessoa('Helena', '15')

#Converte objetos em dicionarios, pois 'dump' não sabe salvar objetos de classe, apenas tipos básicos
bd = [vars(p1), vars(p2), p3.__dict__]

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)

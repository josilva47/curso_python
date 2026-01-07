'''
Pertence à classe, não a uma instância específica

Recebe a própria classe como primeiro parâmetro

Usa cls em vez de self (cls é uma referência à classe Pessoa)

'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('hey')

    #método fábrica
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls):
        return cls('Anônima', 23)
        

p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_sem_nome()
print(p3.nome, p3.idade)
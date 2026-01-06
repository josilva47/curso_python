
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Joao', 'Araujo')

#Métodos em instâncias de classes
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'O {self.nome} esta acelerando')


fusca = Carro('Fusca')
fusca.acelerar()

celta = Carro('Celta')
celta.acelerar()

        

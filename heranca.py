#HERANÇA SIMPLES
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar(self):
        return f'Olá, meu nome é {self.nome} e meu sobrenome é {self.sobrenome}'


class Cliente(Pessoa):
    pass

class Aluno(Pessoa):
    ...

c1 = Cliente('João', 'Araujo')
a1 = Aluno('Rick', 'Almeida')

print(c1.falar())
print(a1.falar())


#HERANÇA MULTIPLA
class A:

    def quem_Sou(self):
        print('A')

class B(A):

    def quem_Sou(self):
        print('B')

class C(A):

    def quem_Sou(self):
        print('C')

class D(B, C):

    def quem_Sou(self):
        print('D')

d = D()
d.quem_Sou()
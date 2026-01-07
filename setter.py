class Pessoa:
    def __init__(self, idade):
        self.idade = idade  # chama o setter

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor #Usamos o (_) atributo interno para nao criar um loop infinito no setter

p = Pessoa(30)
p.idade = 25
print(p.idade)
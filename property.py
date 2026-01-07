'''
@property = um getter no modo Pythonico.
É uma propriedade do objeto, ela é um metodo que se comporta como um atributo, ou seja, permite acessar um método como se fosse um atributo.
Usado como:
- getter
- p/ proteger, validar ou calcular um atributo sem mudar a forma como ele é acessado.
- p/ habilitar setter
- p/ executar acoes ao obter um atributo

'''

#SEM PROPERTY
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

p1 = Pessoa('Joao')
print(p1.get_nome())

#COM PROPERTY
class Caneta:
    def __init__(self, cor):
        self._cor_tinta = cor #underline antes para proteger o valor

    @property
    def cor(self):
        return self._cor_tinta
    
caneta = Caneta('Azul')
print(caneta.cor)

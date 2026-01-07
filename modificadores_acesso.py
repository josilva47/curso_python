'''
Em python esses modificadores não existem. Porem, é uma convenção da comunidade Python

(Sem underline) = public - Pode ser usado em qualquer lugar
(Um underline) = protected - Não deve ser udado fora da classe ou suas subclasses
(Dois underline) = private - Só deve ser usado na classe em que foi declarado
'''

class Foo:
    def __init__(self):
        self.public = 'Isso é publico'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso e privado'

f = Foo()
        
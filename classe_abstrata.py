from abc import ABC, abstractmethod

'''
    Uma classe abstrata em Python é uma classe que não pode ser instanciada diretamente e serve como um modelo/base para outras classes.
    Ela define métodos que devem obrigatoriamente ser implementados pelas classes filhas.
'''

#Essa classe não pode ser instanciada, Ela apenas tera os metodos para as classes filhas
class Animal(ABC):

    @abstractmethod
    def emitir_som(self):
        pass

    def andar(self, animal):
        return f'O {animal} esta andando!'

#Classe filha
class Cachorro(Animal):
    
    def emitir_som(self):
        return 'Au au'
    
c = Cachorro()
print(c.emitir_som())
print(c.andar('Cachorro'))


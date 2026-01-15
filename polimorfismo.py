from abc import ABC, abstractmethod

'''
Polimorfismo acontece quando classes diferentes respondem de forma diferente ao mesmo método, normalmente sobrescrevendo um método da classe pai.
'''

class Animal:

    def falar(self):
        return 'Som generico'
    

class Cachorro(Animal):

    def falar(self):
        return 'Au au'
    
class Gato(Animal):

    def falar(self):
        return "Miauuu"
    

animais = [Cachorro(), Gato()]

for a in animais:
    print(a.falar())

print('=-' * 30)


#EXEMPLO COM CLASSE ABSTRATA
class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        ...

class NotificacaoEmail(Notificacao):

    def enviar(self):
        return f'Enviando E-mail: {self.mensagem}'
    
class NotificacaoSms(Notificacao):

    def enviar(self):
        return f'Enviando SMS: {self.mensagem}'
    

email = NotificacaoEmail('Ola, meu nome é joao')
print(email.enviar())

sms = NotificacaoSms('Estou Chegando!')
print(sms.enviar())
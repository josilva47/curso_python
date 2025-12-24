'''
FUNÇÕES DECORADORAS
Decorar - Adicionar / Remover / Restringir / Alterar
Funções decoradoras sào funções que decoram outras funções
Recebe outra função como argumento 
Retorna uma nova função

DECORADOR
São "Syntax Sugar"

'''

#FUNÇÃO DECORADORA
def criar_funcao(func):

    #Closure
    def interna(*args, **kwargs): #Permite decorar qualquer função
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna

#FUNÇAO ORIGINAL
@criar_funcao #decorador
def inverte_string(string):
    return string[::-1]

#FUNÇÃO DE VALIDAÇÃO
def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')
    

invertida = inverte_string('123')
print(invertida)
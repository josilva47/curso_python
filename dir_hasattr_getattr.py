'''
dir = exibe todos os nome definidos em um objeto - dir(string) <-- no console
hasattr = checa se um objeto tem um determinado nome
getattr = acessa dinamicamente atributos de um objeto

'''

string = 'João'
metodo = 'upper'

# -----EXEMPLO-----
if hasattr(string, 'upper'):
    print('Existe o método Upper na string')
    print(string.upper())
else:
    print('Nào existe o método')

print()
# -----EXEMPLO COM getattr-----
if hasattr(string, metodo):
    print('Existe o método upper na string')
    print(getattr(string, metodo)()) 
else:
    print('Não existe')

print()
# -----EXEMPLO COM VALOR PADRAO getattr-----
get1 = getattr(string, 'upper', lambda: 'não existe')

print(get1())
print(dir(string))
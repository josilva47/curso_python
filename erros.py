""" 
    Introdução ao try/except
    try -> tenta executar o código
    except -> ocorreu algum erro ao tentar executar

"""

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro do {numero_float} é {numero_float * 2}')
except:
    print('Isso não é um numero')
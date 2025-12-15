""" 
    Introdução ao try/except
    try -> tenta executar o código
    except -> ocorreu algum erro ao tentar executar
    finally -> sempre sera executado
    raise -> lança exceções

    link com os tipos de erros -> https://docs.python.org/pt-br/3/library/exceptions.html


"""

try:
    a = 18
    b = 0
    c = a / b
except ZeroDivisionError: # O mais adequado é passar o tipo do erro que pode acontecer
    print('Dividiu por zero')
except NameError:
    print('Variavel nao esta definida')
except Exception as erro: # Todos os tipos de erros
    print('Erro desconhecido')
    print(erro)
finally:
    print('Obrigado por usar nosso sistema')

idade = -5

if idade < 0:
    raise ValueError("Idade não pode ser negativa")



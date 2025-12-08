
def multiplica(*args):
    tot = 1
    for n in args:
        tot *= n
    return tot

numeros = 1, 2, 3, 4, 5

print(multiplica(*numeros)) #  o * desempacota

def par_impar(n):
    condicao =  n % 2 == 0

    return f'O número {n} é PAR' if condicao else f'O número {n} é ÍMPAR'

        
print(par_impar(2))

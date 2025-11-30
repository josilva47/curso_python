
n = input('Digite um numero: ')

if n and n.isdigit():
    if int(n) % 2 == 0:
        print(f'O número {n} é PAR!')
    else:
        print(f'O numero {n} é IMPAR!')
else:
    print('Digite um número inteiro valido!')
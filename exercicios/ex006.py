from time import sleep

n1 = n2 = ''

while True:
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')

    if not (n1.isdigit() and n2.isdigit()):
        print('\033[31mDigite um número valido!\033[m')
        continue

    pn = float(n1)
    sn = float(n2)

    while True:
        operador = input('Qual operação você quer realizar? (+-/x): ').lower().strip()
        if operador not in '+-x/' or len(operador) > 1:
            print('\033[31mOperador invalido! Somente (+) (-) (/) (x)\033[m')
            continue
        else:
            break

    print('\033[32mRealizando sua conta...\033[m')
    sleep(1)
    
        
    if operador == '+':
        print(f'O resultado de {pn} + {sn} é: {pn + sn}')
    elif operador == '-':
        print(f'O resultado de {pn} - {sn} é: {pn - sn}')
    elif operador == 'x':
        print(f'O resultado de {pn} x {sn} é: {pn * sn}')
    elif operador == '/':
        resultado = pn / sn
        print(f'O resultado de {pn} / {sn} é: {resultado:.1f}')

    continuar = ' '
    while continuar not in 'sn':
        continuar = input('Quer continuar? [S/N] ').strip().lower()[0] 
    
    if 'n' in continuar:
        break

print('~' * 40)
print('\033[35mmObrigado por usar a nossa calculadora!\033[m')
print('~' * 40)
 
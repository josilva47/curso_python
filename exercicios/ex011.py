

while True:

    cpf = input('Digite o CPF: ').strip().replace('-', '').replace('.', '')

    if len(cpf) != 11 or not cpf.isdigit() or cpf == (cpf[0] * len(cpf)):
        print('\033[31mCPF inválido!\033[m')
        print('\033[33mExemplo: xxx.xxx.xxx-xx\033[m')
        continue

    # ----- CÁLCULO DO 1º DÍGITO -----
    soma = 0
    contador = 10

    for i in range(9):
        soma += int(cpf[i]) * contador
        contador -= 1
    
    d1 = (soma * 10) % 11
    d1 = 0 if d1 > 9 else d1
    
    if str(d1) != cpf[9]:
        print('\033[31mCPF inválido!\033[m')
        continue

    # ----- CÁLCULO DO 2º DÍGITO -----
    soma = 0
    contador2 = 11

    for i in range(10):
        soma += int(cpf[i]) * contador2
        contador2 -= 1
        
    d2 = (soma * 10) % 11
    d2 = 0 if d2 >= 10 else d2

    if str(d2) == cpf[10]:
        print('\033[32mCPF válido\033[m')
    else:
        print('\033[31mCPF Inválido\033[m')


    # ----- PERGUNTA AO USÚARIO -----
    continuar = ' '
    while continuar not in 'SN':

        continuar = input('Validar outro CPF? [S/N] ').strip().upper()


        if not continuar:
            continuar = ' '
            continue

        continuar = continuar[0]

        if continuar == 'S':
            break

        if continuar == 'N':
            print('Finalizando...')
            exit()



    





    
        



    



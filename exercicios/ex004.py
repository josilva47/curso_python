
hora = input('Digite a hora: ')

if hora and hora.isdigit():
    if 0 <= int(hora) <= 11:
        print('Bom dia!')
    elif 12 <= int(hora) <= 17:
        print('Boa Tarde!')
    else:
        print('Boa noite!')
else:
    print('Digite uma hora válida!')
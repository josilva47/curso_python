
nome = input('Digite seu nome: ').strip()


if nome.isalpha() and nome:
    if len(nome) <= 4:
        print('Seu nome é curto!')
    elif 5 <= len(nome) <= 6:
        print('Seu nome é normal!')
    else:
        print('Seu nome é muito grande!')
else:
    print('Digite um nome válido!')
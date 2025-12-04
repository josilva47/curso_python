from time import sleep

lista = []

while True:
    print('~' * 25)
    print('\033[1;36m' + 'SELECIONE UMA OPÇÃO'.center(25) + '\033[m')
    print('~' * 25)

    opcao = input('[I]Inserir [A]Apagar [L]Listar: ').upper().strip()
    
    if not opcao or opcao[0] not in 'IAL':
        print('\033[33mInsira uma opção válida!\033[m')
        continue

    opcao = opcao[0]
    
    if opcao == 'I':
        item = ' '

        while not item.strip():
            item = input('Item: ').capitalize()

        lista.append(item)
        print('\033[32mItem adicionado com sucesso!\033[m')
        sleep(2)
    elif opcao == 'L':
        if not lista:
            print('\033[33mNão há itens na lista\033[m')
            sleep(1)
            continue

        print('\033[4;34mItens na lista.\033[m')
        for indice, itens in enumerate(lista):
            print(f'{indice} = {itens}')
        sleep(2)
    else:
        apagar_item = input('Escolha o numero do item para remover da lista: ')
        try:
            apagar_item = int(apagar_item)

            for indice, valor in enumerate(lista): 
                if apagar_item == indice:

                    certeza = ' '
                    while certeza not in 'SN':
                        certeza = input(f'\033[1;33mTem certeza que deseja remover {valor} da lista? [S/N]\033[m ').upper().strip()
                        certeza = certeza[0]
                    if certeza == 'S':
                        lista.pop(indice)
                        print(f'\033[32m{valor} removido com sucesso!\033[m')
                    else:
                        print('\033[33mItem não removido!\033[m')
                    break       
            else:
                print('\033[31mItem não encontrado!\033[m')

        except ValueError:
            print('\033[31mDigite um número válido!\033[m')
                






    
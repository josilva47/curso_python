from time import sleep

perguntas = [
    {
        'Pergunta' : 'Quanto é 2 + 2?',
        'Opções' : ['1', '3', '4', '5'],
        'Resposta' : '4',
    },
    {
        'Pergunta' : 'Quanto é 5 x 5?',
        'Opções' : ['25', '55', '10', '51'],
        'Resposta' : '25',
    },
    {
        'Pergunta' : 'Quanto é 10 / 2?',
        'Opções' : ['4', '5', '2', '1'],
        'Resposta' : '5',
    },
]

for p in perguntas:
    
    print(f'\033[1;36mPergunta: {p['Pergunta']}\033[m')
    print()
    print(f'Opções:')
    
    for i, v in enumerate(p.get('Opções'), start=1):
        print(f'{i}) {v}')
    print()

    while True:
        escolha_opcao = input('Escolha uma opção: ')

        if escolha_opcao.isdigit():
            escolha_num = int(escolha_opcao)
            if 1 <= escolha_num <= len(p['Opções']):
                break

        print('\033[31mOpção inválida! Tente novamente.\033[m')

    print('\033[33mVerificando...\033[m')
    sleep(2)

    resposta = p['Opções'][int(escolha_opcao) - 1]

    print('\033[32mAcertou!\033[m' if resposta == p['Resposta'] else '\033[31mErrou!\033[m')
    print()
    sleep(2)
    

    

print('=-' * 15)
print('CONTADOR DE FRASES'.center(30))
print('=-' * 15)

frase = str(input('Digite uma frase: ')).replace(' ', '').lower().strip()

i = 0
apareceu_mais = 0
letra = ''

while i < len(frase):

    frase_iterada = frase[i]

    frase_contada = frase.count(frase_iterada)

    if i == 0:
        apareceu_mais = frase_contada
        letra = frase_iterada
    else:
        if apareceu_mais < frase_contada:
            apareceu_mais = frase_contada
            letra = frase_iterada
    
    i += 1

print(f'\033[36mA letra que mais apareceu foi o "{letra}", ocorrido {apareceu_mais}x\033[m')
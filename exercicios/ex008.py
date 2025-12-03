import os

palavra = 'amor'
tentativas = 0
palavra_formada = ''


while True:
    
    usuario = input('Digite uma letra: ').strip().lower()

    if usuario.isdigit():
        print('\033[31mERRO! Digite APENAS letras!\033[m')
        continue
    elif len(usuario) > 1: 
        print('\033[31mERRO! Dgite APENAS uma letra!\033[m')
        continue

    tentativas += 1

    if usuario in palavra:
        palavra_formada += usuario

        nova_formatada = ''

        for letra in palavra:
            if letra in palavra_formada:
                nova_formatada += letra
            else:
                nova_formatada += '*'

        print(f'\033[34mPalavra formada: \033[1;34m{nova_formatada}\033[m')
    
        if '*' not in nova_formatada:
            os.system('cls')
            print(f'\033[32mPARABENS! Você acertou a palavra secreta "{palavra}" em {tentativas} tentativas!\033[m')
            break
    

    
        
            



        
            






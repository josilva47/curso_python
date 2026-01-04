#Uma função recursiva é uma função que chama a si mesma para resolver um problema.
#A ideia é dividir um problema grande em problemas menores do mesmo tipo, até chegar em um ponto simples que pode ser resolvido diretamente.
#TODA FUNÇAO RECURSIVA DEVE TER:
#Caso base: condiçao ue para a recursão
#Chamada recursiva: A função chama a si mesmo

def contagem(n):
    if n == 0: #Caso base
        print('Fim!')
        return
    
    print(n)
    contagem(n - 1) #Chamada recursiva
    
contagem(5)

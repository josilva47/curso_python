
def concatenar(string_inicial):
    valor_final = string_inicial # é uma variável local da função concatenar (variavel livre)

    def interna(valor_a_concatenar=''): # função interna (closure)
        nonlocal valor_final #Isso diz ao python que 'valor_final' nao e da funcao interna, mas sim, da concatenar e que irei alterar ela
        valor_final += valor_a_concatenar 
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
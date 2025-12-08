def multiplicador(multiplicador):

    def multiplicar(numero):
        return multiplicador * numero
    
    return multiplicar

dobro = multiplicador(2)
print(dobro(4))

triplo = multiplicador(3)
print(triplo(4))



#List comprehension é uma forma rápida para criar listas a partir de iteraveis
#É possivel fazer diversas logicas 

#ESTRUTURA: nova_lista = [expressão for item in iterável if condição]


#Sem list comprehension:
numeros = []
for n in range(5):
    numeros.append(n)
print(numeros)


#Com list comprehension (mesmo código):
numeros = [n for n in range(5)]
print(numeros)

#Multiplicar cada item por 2:
dobros = [n * 2 for n in range(5)]
print(dobros)

#Exemplo com if/else
resultado = ['par' if n % 2 == 0 else 'impar' for n in range(6)]
print(resultado)    
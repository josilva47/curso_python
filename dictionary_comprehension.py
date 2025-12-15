
produto = {
    'nome' : 'Caneta azul',
    'preco' : 2.5,
    'categoria' : 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor # isintance - para saber se o objeto é de determinado tipo
    for chave, valor in 
    produto.items()
}

print(dc)
def sublista_menores(lista, valor):
    sublista = []
    for elemento in lista:
        if elemento < valor:
            sublista.append(elemento)
    return sublista

lista = [1, 5, 2, 8, 3, 10]
valor = 6
resultado = sublista_menores(lista, valor)
print(resultado)  # Output: [1, 5, 2, 3]
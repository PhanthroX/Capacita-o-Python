def multiplicacao_listas(lista1, lista2):
    resultado = []
    for i in range(len(lista1)):
        resultado.append(lista1[i] * lista2[i])
    return resultado

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
resultado = multiplicacao_listas(lista1, lista2)
print(resultado)  # Output: [5, 12, 21, 32]
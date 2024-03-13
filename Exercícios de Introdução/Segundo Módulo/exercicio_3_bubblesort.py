def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
lista = [5, 2, 8, 1, 3]
bubble_sort(lista)
print(lista)  # Output: [1, 2, 3, 5, 8]
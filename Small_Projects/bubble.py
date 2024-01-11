import matplotlib.pyplot as plt

def visualizar(lista):
    plt.bar(range(len(lista)), lista)
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()

def bubble_sort_visual(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                visualizar(lista)
    return lista

# Prueba del algoritmo
lista = []
valor = int(input("Dame un numero: "))
while(valor != 0):
    lista.append(valor)
    valor = int(input("Dame otro numero: "))

print("Lista original:", lista)
print("Lista ordenada:", bubble_sort_visual(lista))

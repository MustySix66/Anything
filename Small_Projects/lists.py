num = int(input("som num: "))
let= str(num)
lista=list(let)
print(lista)
lista.sort()
print(lista)
lista.sort(reverse= True)
print(lista)


# Aqui se hace una lista y se dice el segundo valor más alto
n = int(input())
# aquí se agregan a una lista y se dividen en distintos campos
arr = list(map(int, input().split()))
# Aqui se evitan las entradas duplicadas
arr1 = set(arr)
# Aquí se ordenan
arr2 = sorted(arr1)
# Aquí se imprime el segundo valor mas alto
print(arr2[-2])
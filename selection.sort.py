import random

# Array com 15 números inteiros aleatórios
array = [random.randint(1, 100) for i in range(15)]

print("Array original:")
print(array)

#Primeiro laço
for i in range(len(array)):

    #Variável recebe o valor de i
    menor = i

    #Segundo laço
    for j in range(i + 1, len(array)):

        #Verifica qual elemento possui menor valor
        if array[menor] > array[j]:
            menor = j

    #Troca dos valores
    temp = array[i]
    array[i] = array[menor]
    array[menor] = temp

print("\nArray ordenado:")
print(array)
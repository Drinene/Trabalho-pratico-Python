import random

#Método Bubble Sort
def bubbleSort(array):

    #Primeiro laço
    for i in range(len(array)):

        #Segundo laço
        for j in range(0, len(array) - i - 1):

            #Compara elementos adjacentes
            if array[j] > array[j + 1]:

                #Troca dos valores
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


#Array com 15 números aleatórios
numeros = [random.randint(1, 100) for i in range(15)]

print("Array original:")
print(numeros)

#Aplicando Bubble Sort
bubbleSort(numeros)

print("\nArray ordenado:")
print(numeros)
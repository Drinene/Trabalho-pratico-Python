import time

#Bubble Sort
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array


#Selection Sort
def selectionSort(array):
    for i in range(len(array)):
        menor = i

        for j in range(i + 1, len(array)):
            if array[menor] > array[j]:
                menor = j

        temp = array[i]
        array[i] = array[menor]
        array[menor] = temp

    return array


#Cria lista
palavras = list()

#Lê arquivo linha por linha
with open("loremipsum.txt", "r") as arquivo:

    for linha in arquivo:
        linha = linha.strip()

        #separa em palavras
        palavras_linha = linha.split()

        #adiciona cada palavra na lista
        for palavra in palavras_linha:
            palavras.append(palavra)


#Copiando listas para não alterar a original
listaBubble = palavras.copy()
listaSelection = palavras.copy()
listaSort = palavras.copy()


#Bubble Sort
inicio = time.time()

bubbleSort(listaBubble)

fim = time.time()

print("\n===== Bubble Sort =====")
print(listaBubble)
print("Tempo:", fim - inicio, "segundos")


#Selection Sort
inicio = time.time()

selectionSort(listaSelection)

fim = time.time()

print("\n===== Selection Sort =====")
print(listaSelection)
print("Tempo:", fim - inicio, "segundos")


#Sort nativo
inicio = time.time()

listaSort.sort()

fim = time.time()

print("\n===== Sort Nativo =====")
print(listaSort)
print("Tempo:", fim - inicio, "segundos")


#Salva o método mais rápido (sort)
with open("palavras_ordenadas.txt", "w") as arquivo:

    for palavra in listaSort:
        arquivo.write(palavra + "\n")

print("\nArquivo palavras_ordenadas.txt criado com sucesso!")
import random

# Array com 15 números inteiros aleatórios
numeros = [random.randint(1, 100) for i in range(15)]

print("Array original:")
print(numeros)

# Ordenação crescente
numeros.sort()

print("\nArray ordenado em ordem crescente:")
print(numeros)

# Ordenação decrescente
numeros.sort(key=None, reverse=True)

print("\nArray ordenado em ordem decrescente:")
print(numeros)


# Array de strings
dados = [
    "Vitoria",
    "19/03/2004",
    "123.456.789-00",
    "MG1234567"
]

print("\nArray de strings original:")
print(dados)

# Ordenação crescente
dados.sort()

print("\nArray de strings em ordem crescente:")
print(dados)

# Ordenação decrescente
dados.sort(key=None, reverse=True)

print("\nArray de strings em ordem decrescente:")
print(dados)
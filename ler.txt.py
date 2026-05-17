# Abre o arquivo
arquivo = open("loremipsum.txt", "r")

# Imprime todo o conteúdo
print("Conteúdo completo:")
conteudo = arquivo.read()
print(conteudo)

# Fecha o arquivo
arquivo.close()


# Reabre para imprimir a primeira linha
arquivo = open("loremipsum.txt", "r")

print("\nPrimeira linha:")
print(arquivo.readline())

arquivo.close()


# Reabre para imprimir os 3 primeiros caracteres
arquivo = open("loremipsum.txt", "r")

print("\nPrimeiros 3 caracteres:")
print(arquivo.read(3))

arquivo.close()


# Utilizando with
print("\nUsando WITH:")

with open("loremipsum.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
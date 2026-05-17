#Abre o arquivo texto.txt
arquivo = open("texto.txt", "w")

#Cria a lista
texto = list()

#Adiciona frases na lista
texto.append("Estou aprendendo Python.\n")
texto.append("Manipulação de arquivos é importante.\n")
texto.append("VS Code facilita o desenvolvimento.\n")
texto.append("Esta atividade foi criada com append().\n")

#Escreve o conteúdo da lista no arquivo
arquivo.writelines(texto)

#Fecha o arquivo
arquivo.close()

print("Arquivo criado com sucesso!")
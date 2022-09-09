contador = 0
palavra = "volvo"
nome_arquivo = "discos_estoque.txt"
with open(nome_arquivo, "r") as arquivo:
    for linha in arquivo:
        contador = contador + linha.upper().count(palavra.upper())

print("Palavra pesquisada: " + palavra.upper())
print("Arquivo pesquisado: " + nome_arquivo)
print("Total de palavras encontradas: " + str(contador))

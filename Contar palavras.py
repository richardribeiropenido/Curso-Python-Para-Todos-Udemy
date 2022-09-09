palavras = []

while True:
    palavra = input("Informe uma palavra(ou número zero para sair): ")
    if palavra == "0":
        break
    palavras.append(palavra)

if palavras:
    palavra_contar = input("Informe a palavra que deseja contar: ")
    qtd = palavras.count(palavra_contar)
    print(f"Temos {qtd} ocorrências de {palavra_contar}.")
else:
    print("Nenhuma palavra informada.")

lista_palavras = []
while True:
    palavra = input("Informe uma palavra ou número zero para sair (repita algumas palavras): ")
    if palavra == "0":
        break
    else:
        lista_palavras.append(palavra)
    print(set(lista_palavras))

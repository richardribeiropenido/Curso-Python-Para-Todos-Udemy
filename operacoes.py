import operacoes

lista_numero = []
while True:
    numero = int(input("Informe um número ou zero para sair: "))
    if numero == 0:
        break
    lista_numero.append(numero)

    soma = operacoes.soma(*lista_numero)
    media = operacoes.media(*lista_numero)

    print(f"Soma: {soma}")
    print(f"Media: {media}")

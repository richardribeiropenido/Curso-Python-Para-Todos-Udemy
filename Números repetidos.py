numeros = []
lista_unica = []
lista_repetidos = []

while True:
    numero = int(input("Informe um número (número zero para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

for x in numeros:
    if x not in lista_unica:
        lista_unica.append(x)
    else:
        if x not in lista_repetidos:
            lista_repetidos.append(x)

if numeros:
    print("Números informados: ", numeros)
    print("Números sem repetição: ", lista_unica)
    print("Somente números que se repetiram: ", lista_repetidos)
else:
    print("Nenhum número informado.")



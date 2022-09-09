numeros = []
lista_pares = []
lista_impares = []

while True:
    numero = int(input("Informe um número (número sero para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print("Pares", lista_pares)
print("Ímpares", lista_impares)

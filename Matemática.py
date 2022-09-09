numeros = []
soma = 0
multiplicacao = 1

while True:
    numero = int(input("Informe um número (número zero para sair): "))
    if numero == 0:
        break
        numeros.append(numero)

if numeros:
    for numero in numeros:
        soma += numero
        multiplicacao *= numero
    numeros.sort()
    menor = numeros[0]
    maior = numeros[len(numeros)-1]

    print("Soma: ", soma)
    print("Multiplicação: ", multiplicacao)
    print("Maior número: ", maior)
    print("Menor número: ", menor)

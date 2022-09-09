taxa_juros = 1.2 / 100


def calculo1(num1, num2):
    total = num1 + num2
    total += total * taxa_juros
    print(f"Variaveis locais calculo: {locals()}")
    print(f"Calculo1: {total}")


def calculo2(num1):
    total = 0
    for numero in num1:
        total += numero
    total += total * taxa_juros
    print(f"Variaveis locais calculo2: {locals()}")
    print(f"Calculo2: {total}")


calculo1(25, 14)
numero = [10, 75.5, 96]
calculo2(numero)
print(f"Variaveis globais: {globals()}")

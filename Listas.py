lista_numeros: []

while True:
    numero = float(input("Informe um número ou zero para sair: "))

    if numero == 0:
        break
    else:
        lista_numeros.append(numero)

print("O primeiro número informado foi:", lista_numeros[0])
print("O último número informado foi:", lista_numeros[-1])
print(f"A soma dos números informados é: {sum(lista_numeros):.2f}")
print(f"A média dos números informados é: {sum(lista_numeros) / len(lista_numeros):.2f}")
num_mais = 0
qtd_mais = 1
tem_mais = False
lista_pares = []
lista_impares = []
for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    qtd = lista_numeros.count
    if qtd > qtd_mais:
        tem_mais = True
        qtd_mais = qtd
        num_mais = numero
    if tem_mais:
        print("O número que mais apareceu foi:", num_mais)

    if lista_pares:
        print("Números pares:", lista_pares)
    if lista_impares:
        print("Números ímpares:", lista_impares)
    print("Lista completa:", lista_numeros)
    lista_numeros.reverse()
    print("Lista em ordem inversa:", lista_numeros)
    lista_numeros.sort()
    print("Lista em ordem crescente:", lista_numeros)

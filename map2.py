lista_numeros = [1, 2, 3, 4, 5, 6]
calculo = map(lambda x: f"O quadrado de {x} é: {x ** 2}", lista_numeros)

for n in calculo:
    print(n)

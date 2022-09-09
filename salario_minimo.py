salario_minimo = 1.212


def despesas_fixas():
    agua = 40.00
    luz = 150.00
    despesas = agua + luz
    saldo = salario_minimo - despesas
    print(f"Saldo despesas fixas: {saldo:.2f}")
    return despesas


def despesas_variaveis():
    supermercado = 500.00
    lanchonete = 100.00
    despesas = supermercado + lanchonete
    saldo = salario_minimo - despesas
    print(f"Saldo despesas variaveis: {saldo:.2f}")
    return despesas


def despesas_mes():
    return despesas_fixas() + despesas_variaveis()


print(f"Salário mínimo: {salario_minimo}")
print(f"Despesas Mês: {despesas_mes()}")
valor = 100.00


def calculo():
    valor = 50.00
    print(f"Valor dentro da função: {valor}")
    calculo()
    print(f"Valor fora da função: {valor}")

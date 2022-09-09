salario = float(input("Informe o valor do seu salário: R$ "))
salario_minimo = float(input("Informe o valor do salário mínimo: R$ "))
idade = int(input("Qual a sua idade? "))
resultado = salario > (salario_minimo * 2) and idade > 18
print("O resultado foi", resultado)

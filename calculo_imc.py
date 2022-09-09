nome = input("Digite o seu nome: ")
sexo = input("Informe o sexo 'M' para Masculino e 'F' para Feminino: ")
if sexo != "M" and sexo != "F":
    print("Opção inválida.")
    exit()
peso = float(input("Informe seu peso (KG): "))
altura = float(input("Informe sua altura (M): "))
imc = peso / (altura * altura)
if sexo == "M":
    if imc < 20.7:
        condicao = "Abaixo do peso"
    elif imc <= 26.4:
        condicao = "Peso normal"
    elif imc <= 27.8:
        condicao = "Acima do peso"
    elif imc <= 31.1:
        condicao = "Acima do peso ideal"
    else:
        condicao = "Você está obeso"
elif sexo == "F":
    if imc < 19.1:
        condicao = "Abaixo do peso"
    elif imc <= 25.8:
        condicao = "Peso normal"
    elif imc <= 27.3:
        condicao = "Acima do peso"
    elif imc <= 32.3:
        condicao = "Acima do peso ideal"
    else:
        condicao = "Você esta obeso"
print(f"{nome}, com base no peso e altura informados, " f"o IMC é {imc:.1f} e a condição é '{condicao}'.")

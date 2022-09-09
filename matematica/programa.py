from matematica import operacoes

lista_operacao = ["soma", "subtração", "multiplicação", "divisão", "quadrado", "cubo"]

while True:
    operacao = input("Informe a operação desejada. \n"
                     "1: Soma \n"
                     "2: Subtração \n"
                     "3: Multiplicação \n"
                     "4: Divisão: \n" 
                     "5: Quadrado \n" 
                     "6: Cubo \n"
                     "7: Tabuada \n"
                     "8: Sair ")

    if operacao == "8":
        break
    elif operacao not in ("1", "2", "3", "4", "5", "6", "7"):
        print("Opção inválida!!!")
    else:
        if operacao == "7":
            numero = input("Informe um número inteiro para gerar a tabuada: ")
            if not numero.isdigit():
                print("Número inválido!!!")
            else:
                for t in operacoes.tabuada:
                    print(t(int(numero)))
        else:
        if operacao in ("1", "2", "3", "4"):
            num1 = float(input("Informe o primeiro número: "))
            num2 = float(input("Informe o segundo número: "))
            if operacao == "1":
                resultado = operacoes.soma(float(num1), float(num2))
        elif operacao == "2":
                resultado = operacoes.subtracao(float(num1), float(num2))
        elif operacao == "3":
                resultado = operacoes.multiplicacao(float(num1), float(num2))
        elif operacao == "4":
                resultado = operacoes.divisao(float(num1), float(num2))

        print(f"O resultado da {lista_operacao[int(operacao)-1]} é: {resultado}.")
    else:
    numero = input("Informe o número inteiro para obter um resultado: ")
        if not numero.isdigit():
            print("Número inválido!!!")
        else:
            if operacao == "5":
                resultado = operacoes.quadrado(int(numero))
            elif operacao == "6":
                resultado = operacoes.cubo(int(numero))
        print(f"O resultado do {lista_operacao[int(operacao)-1]} é: {resultado}.")








# Loop infinito while True
while True:
    resposta = input("Você gosta de Python? ")
    if resposta.upper() == "SIM":
        print("A resposta está correta.")
        break
    else:
        print("Opa, está não é a resposta correta, tente novamente.")

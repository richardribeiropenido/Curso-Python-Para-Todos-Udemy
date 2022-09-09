email = "richardpenido@live.com"
indice_arroba = email.index("@")  # impresso 13 caracteres
indice_ponto = email.index(".")  # impresso 19 caracteres
provedor = email[indice_arroba + 1:indice_ponto]  # Foi incrementado 1 para não pegar o arroba
print("O nome do provedor é:", provedor)


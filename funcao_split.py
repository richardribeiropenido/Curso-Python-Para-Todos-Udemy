email = "richardpenido@live.com"
usuario, dominio = email.split("@")
indice_ponto = dominio.index(".")
provedor = dominio[0:indice_ponto]
print("Usuário:", usuario)
print("Domínio:", dominio)

nome = input("Digite seu nome: ")
idade = input("Informe sua idade: ")
cidade = input("Informe sua cidade: ")
frase = nome + idade + cidade
print(f'Seu nome é {nome}, sua idade é de {idade} anos, e você é de {cidade}.'.format(nome, idade, cidade))

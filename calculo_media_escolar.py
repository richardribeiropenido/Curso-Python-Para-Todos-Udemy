nome = input("Digite o nome do aluno: ")
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota : "))
n4 = float(input("Informe a quarta nota: "))
media = (n1+n2+n3+n4)/4
if media < 5:
    resultado = "Reprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Aprovado"
print(f"O aluno {nome} está de {resultado}. "f"Sua média foi {media:.2f}")

def fatorial(x):
    if x <= 1:
        return 1
    else:
        return (x * fatorial(x - 1))


num = int(input("Informe um número para encontrar o fatorial: "))
print("O fatorial de", num, "é", fatorial(num))

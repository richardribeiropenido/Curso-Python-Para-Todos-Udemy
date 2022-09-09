produto = input("Informe o nome do produto: ")
preco = float(input("Informe o preço do produto: R$ "))
quantidade = int(input("Informe a quantidade de produtos: "))
total = preco * quantidade
print("O produto %s custa %.2f, você comprou %d, e vai pagar %.2f." % (produto, preco, quantidade, total))

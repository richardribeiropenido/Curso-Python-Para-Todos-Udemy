valor_parcela = float(input("Digite o valor da parcela mensal : R$ "))
quantidade_meses = int(input("Digite o número de parcelas: "))
valor_compra = valor_parcela * quantidade_meses
print(f"O valor da compra é: R$ {valor_compra:,.2f}")



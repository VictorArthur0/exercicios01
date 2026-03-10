valorDoCarro = 100

numeroDeCarros = int(input("Quantos carros você gostaria de alugar? (cada carro custa R$100 cada): "))

valorTotal = valorDoCarro * numeroDeCarros

print(f"Você quer alugar {numeroDeCarros} carros." )
print(f"Custará {valorTotal}")

respota = input(f"Você tem certeza? (S/N)")
if respota in ['s', 'S']: input("Certo. Obrigado pela Preferência!")
else: input("Certo. Ação cancelada.")
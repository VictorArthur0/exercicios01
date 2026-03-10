preçoPorQuilo = float(input("Qual o preço por quilo do produto? R$ "))

quantidadeKg = float(input("Quantos quilos você quer comprar? "))

preçoTotal = preçoPorQuilo * quantidadeKg

print(f"Preço por quilo: R$ {preçoPorQuilo:.2f}")
print(f"Quantidade comprada: {quantidadeKg:.3f} kg")
input(f"Valor total a pagar: R${preçoTotal:.2f}")
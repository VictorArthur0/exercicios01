
celsius = input("Digite o valor de graus Celsius que deseja converter para Fahrenheit: ")
celsius = float(celsius)

fahrenheit = celsius * 9/5 + 32

print(f"O valor de {celsius}°C inserido, convertido para Fahrenheit fica {fahrenheit:.1f}°F.")
input("Obrigado por usar o programa!")
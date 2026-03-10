import datetime

print("**Dessa vez essa é a calculadora de meses e não de idade**")
anoNasc = int(input("Em que ano você nasceu?: "))
mesNasc = int(input("Em que mês (1-12)? "))
diaNasc = int(input("Em que dia? "))

data_nascimento = datetime.date(anoNasc, mesNasc, diaNasc)
data_atual = datetime.date.today()

idade_meses = (datetime.date.today().year - data_nascimento.year) * 12

input(f"Então você tem {idade_meses} meses!!")
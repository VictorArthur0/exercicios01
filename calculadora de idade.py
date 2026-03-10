import datetime

anoNasc = int(input("Em que ano você nasceu?: "))
mesNasc = int(input("Em que mês (1-12)? "))
diaNasc = int(input("Em que dia? "))

data_nascimento = datetime.date(anoNasc, mesNasc, diaNasc)
data_atual = datetime.date.today()

idade = datetime.date.today().year - data_nascimento.year

if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
    idade -= 1

input(f"Então você tem {idade} anos!!")
# Faça um Programa que peça um número correspondente a um determinado ano e
# em seguida informe se este ano é ou não bissexto.

def bissexto(ano):
    if ano % 4 == 0:
        return "bissexto"
    else:
        return "não é bissexto"

ano = int(input("digite o ano: "))

print(bissexto(ano))
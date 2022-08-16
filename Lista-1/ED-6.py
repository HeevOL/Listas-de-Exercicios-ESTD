# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
# mesma é uma data válida.

dia, mes, ano = input("Digite em formato dd/mm/aaaa: ").split("/")

dia = int(dia)
mes = int(mes)
ano = int(ano)


if dia == 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    print("Data válida")
elif (mes == 2 and dia <= 28) or (mes == 2 and dia == 29 and ano % 4 == 0):
    print("Data válida")
elif mes >= 1 and mes <= 12 and dia <= 30 and mes != 2:
    print("Data válida")
else:
    print("Data inválida")

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
notas = 0
for i in range(1,5,1):
    value = int(input(f'Digite a {i}º nota: '))
    notas = notas + value

print(notas/4)
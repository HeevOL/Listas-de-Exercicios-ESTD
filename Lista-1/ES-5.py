# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

def pesoIdeal(h, sexo):
    if sexo == 'H':
        return (72.7*h) - 58
    else:
        return (62.1*h) - 44.7

altura = float(input("Digite sua altura em metros: "))
sexo = input("Sexo? H - Homi | M - Molier: ")

print(pesoIdeal(altura, sexo))
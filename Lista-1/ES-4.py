# Faça um Programa que peça a temperatura em graus Farenheit, transforme e
# mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9)

def conversorTemp(temp):
    c = (5*(temp-32)/9)
    return c

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
print(conversorTemp(fahrenheit))
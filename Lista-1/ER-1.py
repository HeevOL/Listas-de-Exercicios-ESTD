# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
# caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    value = int(input("Digite um valor válido (de 0 à 10): "))
    if value >= 0 and value <= 10:
        break
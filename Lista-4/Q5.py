# Escreva uma função recursiva que receba um número inteiro positivo N e imprima todos
#  os números naturais de 0 até N em ordem decrescente.

def printNumbers(num):
    if num != -1:
        print(num)
        num = num - 1        
        printNumbers(num)


printNumbers(10)
# Escreva uma função recursiva que receba um número inteiro positivo N e imprima todos 
# os números naturais de 0 até N em ordem crescente.

def printNumbers(num, c=0):
    if num != -1:
        print(num - (num - c))
        c += 1
        num = num - 1        
        printNumbers(num, c)


def printNumbers2(num, c=0):
    if c != num+1:        
        print(c)
        c += 1
        printNumbers2(num, c)


printNumbers(10)
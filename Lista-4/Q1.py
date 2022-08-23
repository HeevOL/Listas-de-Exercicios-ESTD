# Escreva uma função recursiva que calcule e retorne o fatorial de um número inteiro N. Fat(4) = 4 * 3 * 2 * 1

def fatorial(number):
    return number if number == 1 else number * fatorial(number-1)
        

print(fatorial(5))
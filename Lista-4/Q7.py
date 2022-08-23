# Escreva uma função recursiva que receba um número inteiro positivo impar N e retorne
# o fatorial duplo desse número. O fatorial duplo é definido como o produto de todos
# os números naturais ímpares de 1 até algum número natural ímpar N.
# Assim, o fatorial duplo de 5 é 5!! == 1 * 3 * 5 = 15

def doubleFactorial(num):
    if num%2 == 0:
        return "Parâmetro da função deve ser Ímpar!"
    else:
        return num if num == 1 else num * doubleFactorial(num - 2)
            

def doubleFactorial2(num):
    return "Parâmetro da função deve ser Ímpar!" if num%2 == 0 else num if num == 1 else num * doubleFactorial2(num - 2)

        
print(doubleFactorial2(5))
# Escreva uma função recursiva que receba um número inteiro positivo impar N e retorne
# o fatorial duplo desse número. O fatorial duplo é definido como o produto de todos
# os números naturais ímpares de 1 até algum número natural ímpar N.
# Assim, o fatorial duplo de 5 é 5!! == 1 * 3 * 5 = 15

def doubleFactorial(num):
    if num%2 == 0:
        return "Parâmetro da função deve ser Ímpar!"
    else:
        if num == 1:
            return num
        else:
            return num * doubleFactorial(num - 2)


print(doubleFactorial(9))
# Faça uma função fatorial(n) que, dado um número N, calcule e retorne o fatorial de N. O fatorial de um
# número natural n,representado por n!, é o produto de todos os inteiros positivos menores ou iguais a n. 
# Exemplos: 5! = 1 x 2 x 3 x 4 x 5 = 120 0! = 1

def fatorial(n):
    fat = n
    while n != 1:
        n -= 1
        fat *= n
        
    return fat

print(fatorial(5))
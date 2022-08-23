# Escreva uma função recursiva que calcule o Nésimo 10 termo da sequencia de Fibonacci.
#  A sequência de Fibonacci é 0,1, 1, 2, 3, 5, 8, 13, 21,...

def fibonacci(num, fib=[0, 1], c = 2):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    elif num == c:
        return fib[len(fib)-1]
    else:
        fib.append(fib[-2+c]+fib[-1+c])
        c += 1
        return fibonacci(num, c=c)


def fibonacci2(num, n1=0, n2=1, next=1):
    if num == 1:
        return 0
    elif num == 2:
        return next
    else:
        next = n1 + n2
        n1 = n2
        n2 = next        
        return fibonacci2(num-1,n1,n2,next)


print(fibonacci2(9))
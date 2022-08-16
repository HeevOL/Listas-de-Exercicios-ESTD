# Faça um Programa que leia três números e mostre o maior e o menor deles.

def maior(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

def menor(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    elif n2 <= n1 and n2 <= n3:
        return n2
    else:
        return n3

n1, n2, n3 = input("Digite os 3 números: ").split()

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

print(maior(n1, n2, n3))
print(menor(n1, n2, n3))
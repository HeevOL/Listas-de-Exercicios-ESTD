# Faça um programa que leia 5 números e informe o maior número.

n = int(input())
maior = n
for i in range(0,4):
    n = int(input())
    if n > maior:
        maior = n

print(maior)
    

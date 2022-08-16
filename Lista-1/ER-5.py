# Faça um programa que leia 5 números e informe a soma e a média dos números.

sum = 0

for i in range(0,5):
    number = int(input())
    sum += number

print(f'Soma: {sum}')
print(f'Média: {sum/5}')
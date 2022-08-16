# Faça uma função maior_de_3(num1, num2, num3)que, dados três números, retorna o maior deles.

def maior_de_3(num1, num2, num3):
    if num1 >= num2 and num1 >=num3: return num1
    elif num2 >= num1 and num2 >= num3: return num2
    else: return num3


print(maior_de_3(9,9,9))
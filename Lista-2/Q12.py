# Faça uma função eh_primo(numero) que recebe como parâmetro um número inteiro e retorna True se ele é 
# um númeroprimo e False caso contrário. Um número é primo quando ele é divisível somente por um e por 
# ele mesmo.

def eh_primo(num):
    divisor = num

    while divisor != 2:
        divisor = divisor - 1
        if num % divisor == 0:
            return False

    return True   

print(eh_primo(109))


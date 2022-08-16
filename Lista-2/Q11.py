# Faça uma função soma_numeros(numero) que recebe como parâmetro um número N, calcula a soma de todos os 
# númerosde 1 até ele e retorna o valor da soma. Exemplo: soma_numeros(7) = 28 , pois 1+2+3+4+5+6+7=28.

def soma_numeros(numero):
    soma = 0
    for i in range(1,numero+1):
        soma += i
    return soma

print(soma_numeros(8))
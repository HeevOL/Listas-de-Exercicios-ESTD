# A sequência de Fibonacci é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual,
# cada termosubsequente corresponde a soma dos dois anteriores. Faça uma função Fibonacci(termo) que dado 
# um número N representando o n-ésimo termo da sequencia de Fibonacci, retorna a soma desses termos. Exemplo: 
# Fibonacci(7) = 20 ,pois os 7 primeiros termos da sequencia de Fibonacci são “0,1, 1, 2, 3, 5, 8” e sua 
# soma é 20

def fibonacci(termo):
    soma = 1
    n1 = 0
    n2 = 1
    n3 = 1
    for i in range(termo-2):
        n3 = n1+n2
        n1 = n2
        n2 = n3
        soma += n3

    return soma

print(fibonacci(7))
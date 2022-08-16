# Questão 1 - 

# *François-Édouard-Anatole Lucas* (1842-1891) foi um matemático francês e popularizou os Números de Fibonacci em sua obra
# *Recherches Sur Plusierurs Ouvrages de Léonard de Pisa* (1877). Nessa obra ele criou outra sequência semelhante:
# 2, 1, 3, 4, 7, 11, 18,...

# Note que a partir do 3o termo, cada elemento da sequência é a soma dos dois anteriores.

# Escreva uma função em python que, dado um número N, retorna uma lista com os N primeiros termos dessa sequência.

# Exemplo de entrada: sequencia(7)

# Saída esperada: [2, 1, 3, 4, 7, 11, 18, ]

def sequencia(value):
    if value == 1:
        return [2]
    elif value == 2:
        return [2, 1]
    else:
        seq = [2, 1]
        for i in range(0,value-2):
            seq.append(seq[i]+seq[i+1])
        return seq


print(sequencia(7))
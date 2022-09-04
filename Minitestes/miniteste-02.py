# Escreva uma função recursiva que repete "sil" ao final da palavra "Brasil" de acordo com
# o numero dado como parametro da função.

# Entregue:
def repeteSilaba(num, word="Bra"):
    if num == 0:
        return word
    else:
        word = word + "sil"
        return repeteSilaba(num-1, word)

# Melhorado:
def repeteSilaba2(num): return "Brasil" if num <= 1 else repeteSilaba2(num-1) + "sil"

print(repeteSilaba(6))
print(repeteSilaba2(5))
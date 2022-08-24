# Escreva uma função recursiva que repete "sil" ao final da palavra "Brasil" de acordo com
# o numero dado como parametro da função.

def repeteSilaba(num, word="Bra"):
    if num == 0:
        return word
    else:
        word = word + "sil"
        return repeteSilaba(num-1, word)


def repeteSilaba2(num): return "Bra" if num == 0 else repeteSilaba2(num-1) + "sil"

print(repeteSilaba(6))
print(repeteSilaba2(5))
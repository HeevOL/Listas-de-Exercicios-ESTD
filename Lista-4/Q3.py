# Escreva uma função recursiva que determine quantas vezes uma letra K ocorre em uma Palavra P. Por exemplo, a letra 'u'
# ocorre 2 vezes em "estrutura"

def countCharInWord(word, char):
    if len(word) == 0:
        return 0
    else:
        if word[0] == char:
            return 1 + countCharInWord(word[1:], char)
        else:
            return countCharInWord(word[1:], char)


def countCharInWord2(word, char):
    if len(word) == 0:
        return 0
    else:
        return 1 + countCharInWord2(word[1:], char) if word[0] == char else countCharInWord2(word[1:], char)


print(countCharInWord("estrutura", "u"))
print(countCharInWord2("estrutura", "u"))
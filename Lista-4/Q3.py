# Escreva uma função recursiva que determine quantas vezes uma letra K ocorre em uma Palavra P. Por exemplo, a letra 'u'
# ocorre 2 vezes em "estrutura"

def countCharInWord(word, char):
    if len(word) == 0:
        return 0
    else:
        if word[0] == char:
            word = word[1:]
            return 1 + countCharInWord(word, char)
        else:
            word = word[1:]
            return countCharInWord(word, char)


print(countCharInWord("estrutura", "u"))
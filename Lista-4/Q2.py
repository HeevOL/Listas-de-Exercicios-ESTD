# Escreva uma função recursiva que permita inverter uma palavra N. "Python" -->> "nohtyP"

def inversor(word):
    inverted_word = ""
    if len(word) == 0:
        return inverted_word
    else:
        inverted_word = word[len(word)-1]
        return inverted_word + inversor(word[:len(word)-1])


def inversor2(word):
    return word if len(word) == 0 else inversor2(word[1:]) + word[0]

    
print(inversor2("Heverton"))

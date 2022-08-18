# Escreva uma função recursiva que informa se uma String é palíndroma ou não. 
# Um palíndromo é uma string que é lida da mesma maneira da esquerda para a direita
# e da direita para a esquerda. Alguns exemplos de palíndromo são "E até o
# papa poeta é" (se os espaços, pontuação e acentos forem ignorados).


def verifyPalindrome(string:str, inverted_string="", c=1):
    
    if len(string) == len(inverted_string):
        if string == inverted_string:
            return True
        else: return False
    else:
        inverted_string = inverted_string + string[len(string)-c]
        c += 1
        return verifyPalindrome(string.replace(" ",''), inverted_string=inverted_string, c=c)           


print(verifyPalindrome("e ate o papa poeta e"))
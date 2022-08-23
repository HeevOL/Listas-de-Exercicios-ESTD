# Escreva uma função recursiva que informa se uma String é palíndroma ou não. 
# Um palíndromo é uma string que é lida da mesma maneira da esquerda para a direita
# e da direita para a esquerda. Alguns exemplos de palíndromo são "E até o
# papa poeta é" (se os espaços, pontuação e acentos forem ignorados).


def verifyPalindrome(string:str, inverted_string="", c=1):    
    if len(string) == len(inverted_string):
        return True if string == inverted_string else False
    else:
        inverted_string = inverted_string + string[len(string)-c]
        c += 1
        return verifyPalindrome(string.replace(" ",''), inverted_string=inverted_string, c=c)


def verifyPalindrome2(string):
    string = removeEspacos(string)
    if len(string) <= 1:
        return True
    else:
        return False if string[0] != string[-1] else verifyPalindrome2(string[1:-1])


def removeEspacos(string):
    if string[0] == " " and string[-1] == " ":
        return string[1:-1]
    elif string[0] == " ":
        return string[1:]
    elif string[-1] == " ":
        return string[:-1]
    else:
        return string


print(verifyPalindrome2("e ate o papa poeta e"))
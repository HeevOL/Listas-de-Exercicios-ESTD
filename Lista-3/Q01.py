# Uma palavra é palíndroma se ela não se altera quando lida da direita para esquerda. Por exemplo, 
# raiar é palíndroma.Escreva um programa que verifique se uma palavra dada é palíndroma.

def palindroma(string):
    string_invertida = ""
    for i in range(1,len(string)+1):
        string_invertida += string[len(string)-i]
    
    return True if string_invertida == string else False


print(palindroma("raiar"))
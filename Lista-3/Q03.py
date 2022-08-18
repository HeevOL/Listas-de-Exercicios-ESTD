# Escreva uma função que recebe uma string e imprime somente a última palavra da mesma. 
# Exemplo: Se a string digitadafor "José da Silva", deverá ser impresso na tela a substring "Silva"

def lastWord(string):
    for i in range(1, len(string)+1):
        if string[len(string)-i] == " ":
            return string[len(string)-i+1:]


print(lastWord("José da Silva"))
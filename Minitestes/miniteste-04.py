# Aqui do jeito que o professor fez.
def checkPassword(senha:str):    
    if senha[0].islower() or senha[-1].isupper():
        return "Inválida"
    
    pilha = []
        
    for char in senha:
        if char.isupper():
            pilha.append(char) # Sei que não é um push mas nesse caso está tendo o mesmo comportamento
        elif char.upper() == pilha.pop():
            pass
        else:
            return "Inválida"

    return "Válida"


# Aqui o jeito que eu pensei.
def checkPassword2(senha:str):
    if senha[0].islower() or senha[-1].isupper():
        return "Inválida"
        
    pilha = []
    for char in senha:
        pilha.append(char)    
        
    lista = []
    for i in range(len(senha)):
        if str(pilha[-1]).islower(): # Como não possuo uma classe com a função top() estou utilizando a posição equivalente.
            lista.append(pilha.pop()) # Sei que não é um push mas nesse caso está tendo o mesmo comportamento
        elif str(lista[-1]).upper() == pilha.pop():
            lista.pop()
        else:
            return "Inválida"

    return "Válida"               

print(checkPassword2("Aa")) 
print(checkPassword2("aA"))
print(checkPassword2("AB"))
print(checkPassword2("Ab"))
print(checkPassword2("ABba"))
print(checkPassword2("ABab"))
print(checkPassword2("ABbCca"))
print(checkPassword2("ABCcDEedba"))
print(checkPassword2("BRrAba"))
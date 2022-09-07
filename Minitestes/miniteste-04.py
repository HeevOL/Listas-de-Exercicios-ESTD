# Segurança na copa do Mundo

# Preocupado com a segurança cibernética na copa do mundo, a organização contratou uma empresa para definir regras para
# escrita das senhas. As regras abaixo são uma proposta em estudo. Escreva uma função em python para determinar se uma senha
# atende ou não as regras propostas.

# Regras para as senhas

# 1. Podem ser utilizadas somente letras Maiúsculas ou minúsculas.
# 2. Deve sempre começar com letras Maiúsculas.
# 3. Para cada letra Maiúscula deve haver na senha uma letra minúscula equivalente
# 4. As letras Maiúsculas podem aparecer em qualquer ordem na senha.
# 5. As letras minúsculas devem aparecer na ordem inversa de aparição das letras Maiúsculas equivalentes.

# Exempos de senhas válidas e inválidas
#   Aa          válida
#   aA          inválida
#   AB          inválida
#   Ab          inválida
#   ABba        válida
#   ABab        inválida
#   ABbCca      válida
#   ABCcDEedba  válida
#   BRrAba      inválida

class PilhaVazia(Exception):
    pass


class Pilha():
    def __init__(self):
        self._pilha = []

    def top(self):
        if self.is_empty():
            raise PilhaVazia('A pilha está vazia')
        return self._pilha[-1]

    def is_empty(self):
        return len(self._pilha) == 0

    def pop(self):
        if self.is_empty():
            raise PilhaVazia('A pilha está vazia')
        return self._pilha.pop()

    def push(self, e):
        self._pilha.append(e)

    def size(self):
        return self.__len__()

    def __len__(self):
        return len(self.pilha)


# Aqui do jeito que o professor fez.
def checkPassword(senha:str):    
    if senha[0].islower() or senha[-1].isupper():
        return "Inválida"
    
    pilha = Pilha()
        
    for char in senha:
        if char.isupper():
            pilha.push(char)
        elif char.upper() == pilha.pop():
            pass
        else:
            return "Inválida"

    return "Válida"


# Aqui o jeito que eu pensei.
def checkPassword2(senha:str):
    if senha[0].islower() or senha[-1].isupper():
        return "Inválida"
        
    senha_pilha = Pilha()
    for char in senha:
        senha_pilha.push(char)    
        
    pilha_minusculos = Pilha()
    for i in range(len(senha)):
        if senha_pilha.top().islower():
            pilha_minusculos.push(senha_pilha.pop())
        elif pilha_minusculos.pop().upper() == senha_pilha.pop():
            pass
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
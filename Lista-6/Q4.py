# 4. Desenvolva uma função que inverte uma lista de elementos colocando-os todos em uma pilha, e colocando-os novamente
# na lista de forma invertida.

def inverter(l):
    stack = []
    for i in range(len(l)):
        stack.append(l.pop(0))
    for i in range(len(stack)):
        l.append(stack.pop())
    return l


lista = [1,2,3,4,5,6,7]
inverter(lista)
print(lista)
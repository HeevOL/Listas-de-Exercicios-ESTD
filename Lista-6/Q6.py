# 6. Crie uma função que copia todos os elementos de pilha p para outra pilha q, de forma que os elementos mantenham a
# mesma ordem, ou seja, o elemento no topo da pilha p permanecerá no topo da pilha q

def stackCopy(pilha, copia=[]):
    if len(pilha) == 0:
        return pilha
    temp = pilha.pop()
    stackCopy(pilha)
    copia.append(temp)
    pilha.append(temp) # Refiz a pilha para que a original tbm possa ser usada no programa.
    return copia

l = [1,2,3,4,5,6]
print(stackCopy(l))
print(l)
    
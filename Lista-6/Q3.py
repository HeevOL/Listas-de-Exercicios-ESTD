# 3. Desenvolva um método/função recursiva para remover todos os elementos de uma pilha.

def stackCleaner(stack):
    if stack == []:
        return stack
    stack.pop()
    return stackCleaner(stack)

p = [1,2,3,4]
stackCleaner(p)
print(p)
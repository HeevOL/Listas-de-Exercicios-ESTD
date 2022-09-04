# 5. Mofique a implementação PilhaArray para que a capacidade da pilha seja limitada a uma quantidade MAX de elementos,
# onde MAX será um parâmetro opcional do construtor (init). Se push for chamado quando a pilha estiver cheia, uma
# exceção deve ser lançada. Crie também a função is_full().


class PilhaVazia(Exception):
    pass

class PilhaCheia(Exception):
    pass

class PilhaArray:
    def __init__(self, MAX=10):
        self.pilha = []
        self.MAX = MAX

    def __str__(self): return str(self.pilha)

    def __len__(self): return len(self.pilha)    

    def push(self, value):
        if self.is_full():
            raise PilhaCheia('A pilha está cheia.')            
        return self.pilha.append(value)

    def is_full(self): return True if len(self.pilha) == self.MAX else False
        
    def is_empty(self): return True if len(self.pilha) == 0 else False

    def pop(self):
        if self.is_empty():
            raise PilhaVazia('A pilha está vazia.')
        else:
            return self.pilha.pop()

    def top(self):
        if len(self.pilha) == 0:
            return self.is_empty()
        else:
            return self.pilha[len(self.pilha)-1]

if __name__ == '__main__':
    pilha = PilhaArray(MAX=4)
    pilha.push(4)
    pilha.push(3)
    pilha.pop()
    pilha.push(5)
    pilha.push(6)
    pilha.push(7)
    print(pilha.top())
    # pilha.push(8)
    pilha.pop()
    pilha.pop()
    pilha.pop()
    # pilha.pop()
    # pilha.pop()
    print(len(pilha))
    print(pilha)

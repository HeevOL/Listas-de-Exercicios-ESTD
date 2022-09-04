# 1. Sobre o conceito de Tipos Abstrato de Dado, assinale a alternativa falsa:
# [ ] Conjunto de valores e série de operações que podem ser aplicadas aos valores
# [ ] Especifica as características relevantes das entidades de um tipo e como manipulá-las
# [ ] São os tipos encontrados nas linguagens de programação
# [ ] Permitem a criação de novos tipos de dados
# 2. Para a implemenentação do TAD Lista Candidatos 1, discutida em aula, qual a diferença de desempenho das funções
# adiciona_na_posicao() e adiciona():
# [ ] em ambas o tempo gasto para inserir um elemento é proporcional a quantidade de elementos
# [X] nessa implementação, adiciona() é mais eficiente do que adiciona_na_posicao()
# [ ] adiciona_na_posicao() tem um tempo constante, enquanto em adiciona() o tempo é proporcional a quantidade de elementos
# [ ] em ambas o tempo gasto para adicionar um elemento é constante
# 3. Para a implemenentação do TAD Lista Candidatos 2, discutida em aula, qual a diferença de desempenho das funções
# adiciona_na_posicao() e adiciona():
# [ ] em ambas o tempo gasto para inserir um elemento é proporcional a quantidade de elementos.
# [X] nessa implementação, adiciona() é mais eficiente do que adiciona_na_posicao().
# [ ] adiciona_na_posicao() tem um tempo constante, enquanto em adiciona() o tempo é proporcional a quantidade deelementos.
# [ ] em ambas o tempo gasto para adicionar um elemento é constante.
# 4. Escreva código python que:
# Crie um tipo de dados Conta que armazena 'numero_conta', 'nome_correntista', 'saldo'
# Pergunte ao usuário vários números de contas e os armazene em uma lista
# Após armazenar, escreva todas as contas na tela
# Escreva a conta com o maior saldo
#---------------------------------------------------------------------------------------------------------------------------#

# Nessa classe o acesso as informações são sequenciais e menos intuitivas de se guardar a informação. As informações da
# primeira conta registrada ficara nas 0, 1 e 2. A proxima conta nas posições 3, 4 e 5.

class Conta:
    def __init__(self):
        self.contas = []

    def __str__(self):
        self.retorno = 'Contas registradas:\n'      
        for i in range(0,len(self.contas),3):
            self.retorno += (f'Nº conta: {self.contas[i]}, Titular: {self.contas[i+1]}, Saldo: {self.contas[i+2]}\n')
        
        return self.retorno

    def __len__(self):
        return len(self.contas/3)

    def maior_saldo(self):
        maior = ['','',0]
        for i in range(2,len(self.contas),3):
            if maior[2] < self.contas[i]:
                maior.clear()
                maior.append(self.contas[i-2])
                maior.append(self.contas[i-1])
                maior.append(self.contas[i])
        return f'Conta com maior saldo:\nNº conta: {maior[0]}, Titular: {maior[1]}, Saldo: {maior[2]}'

    def adiciona_conta(self, num, nome, saldo):
        self.contas.append(num)
        self.contas.append(nome)
        self.contas.append(saldo)
#---------------------------------------------------------------------------------------------------------------------------#

# Nessa classe o acesso as contas são feitas por index sequenciais e seus valores de nº da conta, nome correntista e saldo
# são feitos pelos index 0, 1 e 2 respectivamente ex.: conta[0][1] retorna o nome do correntista da primeira conta cadastrada.

class Conta2:
    def __init__(self):
        self.contas = []

    def __str__(self):
        self.retorno = ''      
        for i in range(len(self.contas)):
            self.retorno += (f'{i}: [{self.contas[i][0]}, {self.contas[i][1]}, {self.contas[i][2]}]\n')
        
        return self.retorno

    def __len__(self):
        return len(self.contas)

    def maior_saldo(self):
        maior = ['','',0]
        for i in range(len(self.contas)):
            if maior[2] < self.contas[i][2]:
                maior.clear()
                maior.append(self.contas[i][0])
                maior.append(self.contas[i][1])
                maior.append(self.contas[i][2])
        return f'Conta com maior saldo:\nNº conta: {maior[0]}, Titular: {maior[1]}, Saldo: {maior[2]}'

    def adiciona_conta(self, num, nome, saldo):
        self.contaTemp = []
        self.contaTemp.append(num)
        self.contaTemp.append(nome)
        self.contaTemp.append(saldo)
        self.contas.append(self.contaTemp)
#---------------------------------------------------------------------------------------------------------------------------#

# Main

if __name__ == '__main__':
    entrada = ''
    contas = Conta()
    # contas = Conta2()
    while entrada != 'sair':
        entrada = input('Digite o número da conta, nome do correntista e o saldo da conta: ')
        if entrada != 'sair':
            num, nome, saldo = entrada.split()
            contas.adiciona_conta(num, nome, int(saldo))

    print(contas)
    print(contas.maior_saldo())
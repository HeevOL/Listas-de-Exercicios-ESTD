# A copa do mundo vem aí!Crie um novo tipo de dado chamado Jogo. Esse tipo de dado deve armazenar o nome dos dois times 
# (ou seleções) e aquantidade de gols marcado por cada time. Deve ainda permitir informar a alteração do placar conforme 
# exemplo. Por último,deve permitir informar o vencedor da partida e o placar final.
# exemplo de uso
# jogo=Jogo('Brasil', 'Argentina')
# jogo.gol_time_1()
# jogo.gol_time_2()
# jogo.gol_time_1()
# print(jogo.vencedor()) #Brasilprint
# (jogo.placar())   #Brasil (2) x (1) Argentina
# print(jogo)       #Brasil (2) x (1) Argentina

class Jogo:
    def __init__(self, time1, time2):
        self.time1 = time1
        self.time2 = time2
        self.gols_t1 = 0
        self.gols_t2 = 0

    def __str__(self): return f'{self.time1} ({self.gols_t1}) x ({self.gols_t2}) {self.time2}'

    def gol_time_1(self): self.gols_t1 += 1

    def gol_time_2(self): self.gols_t2 += 1

    def vencedor(self): return self.time1 if self.gols_t1 > self.gols_t2 else self.time2 if self.gols_t1 < self.gols_t2 else "Empate"

    def placar(self): return self.__str__()


if __name__ == '__main__':
    jogo=Jogo('Brasil', 'Argentina')
    jogo.gol_time_1()
    jogo.gol_time_2()
    jogo.gol_time_1()
    # jogo.gol_time_2()
    print(jogo.vencedor())  #Brasil
    print(jogo.placar())    #Brasil (2) x (1) Argentina
    print(jogo)             #Brasil (2) x (1) Argentina


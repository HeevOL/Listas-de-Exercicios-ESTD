# Faça um programa para a leitura de duas notas parciais de um aluno. O programa
# deve calcular a média alcançada por aluno e apresentar:
# A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
# A mensagem “Reprovado”, se a média for menor do que sete;
# A mensagem “Aprovado com Distinção”, se a média for igual a dez.

def msg(media):
    if media == 10:
        return ("Aprovado com Distinção")
    elif media >= 7:
        return ("Aprovado")
    else:
        return ("Reprovado")


nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))

media = (nota1+nota2)/2

print(msg(media))
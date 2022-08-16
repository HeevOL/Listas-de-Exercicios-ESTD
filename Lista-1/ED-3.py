# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

def diaDaSemana(dia):
    if   dia == 1: return "Domingo"
    elif dia == 2: return "Segunda"
    elif dia == 3: return "Terça"
    elif dia == 4: return "Quarta"
    elif dia == 5: return "Quinta"
    elif dia == 6: return "Sexta"
    elif dia == 7: return "Sábado"
    else: return "valor inválido"

value = int(input())

print(diaDaSemana(value))
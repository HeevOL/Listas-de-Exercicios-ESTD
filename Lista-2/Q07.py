# Faça uma função dia_da_semana(dia) que recebe como parâmetro um número e retorna o dia correspondente da
# semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve retornar valor inválido

def dia_da_semana(day):
    if day == 1: return "Domingo"
    elif day == 2: return "Segunda"
    elif day == 3: return "Terça"
    elif day == 4: return "Quarta"
    elif day == 5: return "Quinta"
    elif day == 6: return "Sexta"
    elif day == 7: return "Sábado"
    else: return "Valor inválido"


print(dia_da_semana(5))
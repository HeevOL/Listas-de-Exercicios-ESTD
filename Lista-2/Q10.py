# Faça uma função eh_data_valida(dia, mes, ano) que recebe como parâmetro três valores, 
# representando dia, mês e ano.Essa função deve retornar True se os valores formarem uma data 
# válida, e False caso contrário

def eh_data_valida(dia, mes, ano):
    if dia == 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        return True
    elif (mes == 2 and dia <= 28) or (mes == 2 and dia == 29 and ano % 4 == 0):
        return True
    elif mes >= 1 and mes <= 12 and dia <= 30 and mes != 2:
        return True
    else:
        return False


print(eh_data_valida(29,2,1996))
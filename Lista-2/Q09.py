# Faça uma função eh_bissexto(ano) que recebe um ano como parâmetro e retorna True se o ano for bissexto e 
# False casocontrário
def eh_bissexto(ano): return True if ano % 4 == 0 else False


print(eh_bissexto(2022))
# Faça uma função hipotenusa(cateto1, cateto2) que retorna o comprimento da hipotenusa de um triângulo 
# retângulo dados os comprimentos dos dois lados como parâmetros.

from math import sqrt


def hipotenusa(cat1, cat2): return sqrt(cat1**2 + cat2**2)


print(hipotenusa(9,12))
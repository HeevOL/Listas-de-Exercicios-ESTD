# Faça um programa que leia um nome de usuário e a sua senha e não aceite a
# senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
# pedir as informações.
user = input("Usúario: ")
password = input("Senha: ")

while user == password:   
    print("Usuário e senha iguais, digite valores distintos!\n")
    user = input("Usuário: ")
    password = input("Senha: ")

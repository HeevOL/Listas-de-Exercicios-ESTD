# As companhias de transportes aéreos costumam representar os nomes dos passageiros no 
# formato último sobrenome/nome. Por exemplo, o passageiro Carlos Drumond de Andrade seria 
# indicado por Andrade/Carlos. Escreva um programa que lê um nome e o escreve no formato acima.

def nameFormat(name):
    last_name = ""
    first_name = ""
    for i in range(1,len(name)):
        if name[len(name)-i] == " ":
            last_name = name[len(name)-i+1:]
            break
    
    for i in range(0,len(name)):
        if name[i] == " ":
            first_name = name[:i]
            break
    
    return last_name+"/"+first_name


print(nameFormat(input("Digite seu nome: ")))

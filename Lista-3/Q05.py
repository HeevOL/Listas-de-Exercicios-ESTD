# As normas para a exibição da bibliografia de um artigo científico, de uma monografia, de 
# um livro texto, etc., exigem que o nome do autor seja escrito no formato último sobrenome, 
# sequência das primeiras letras do nome e dos demais sobrenomes, seguidas de ponto final. 
# Por exemplo, Antônio Carlos Jobim seria referido por Jobim, A. C.. Escreva um programa que 
# receba um nome e o escreva no formato de bibliografia

def nameArticleFormat(name:str):
    last_name = ""
    space_index_last_name = 0
    nickname_letters = ""
    for i in range(1, len(name)-1):
        if name[len(name)-i] == " ":
            last_name = name[len(name)-i+1:]
            space_index_last_name = len(name)-i
            break
    
    for i in range(0, space_index_last_name):
        if name[i] == " " and name[i+1].isupper():
            nickname_letters += name[i+1]+". "
    
    return last_name + ", " + name[0] + ". " + nickname_letters[:len(nickname_letters)-1]



print(nameArticleFormat(input("Nome: ")))
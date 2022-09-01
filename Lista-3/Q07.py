def login(name:str):
    names = []
    names.extend(name.split())

    login = ""
    for name in names:     
        if name[0].isupper(): 
            login += name[0].lower()

    return login

print(login("Heverton de Oliveira Lourenço"))
def wordChanger(string:str, be_removed, be_inserted):  
      
    if be_removed in string:
        string = string.replace(be_removed, be_inserted)
    return string


print(wordChanger("Heverton de Oliveira Lourenço", "Oliveira", "Andrade"))
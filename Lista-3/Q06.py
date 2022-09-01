
def docFormat(string):
    words = []
    words.extend(string.split())

    doc_format = ""
    for word in words:     
        if word[0].isupper(): 
            doc_format += word[0] + " "

    return doc_format[:-1]
    

print(docFormat("Atestado de Matricula da Universidade Federal de Alagoas"))

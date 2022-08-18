# Um dos recursos disponibilizados pelos editores de texto mais modernos é a determinação do número de 
# palavras de um texto. Escreva um programa que determine o número de palavras de um texto dado

def qntdWords(text): # Conta baseado nos espaços do texto
    if text == "": return 0
    word_counter = 0
    for i in range(len(text)-1):
        if text[i] == " ":
            word_counter += 1
    return word_counter + 1


print(qntdWords("Isso dá certo se o usuario digitar de forma correta, colocar mais de 1 espaço entre palavras ou no fim do texto já dá errado."))
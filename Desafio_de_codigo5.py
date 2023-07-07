def reverter(palavra):  # função para reverter a palavras

    palavra_rev = palavra[::-1]  # reverte a ordem das palavras

    return palavra_rev  # retorna a frase completa revertida

palavra_original = input("Digitar a frase: ")  # recebe a frase digitada para verificação

string_nova = reverter(palavra_original)  # chama a função para reverter a frase

if (string_nova == palavra_original): # verificar se as palavras são iguais, tanto no original quanto revertidas
    print("Essa string é palíndroma: ", string_nova) # caso verdadeiro, imprime a frase

else:
    print("String NÃO é palíndroma: ", string_nova) # caso falso, imprime essa frase



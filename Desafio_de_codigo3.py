def verif_palindroma(palavra):  # função para verificar a substring palíndroma mais longa

    palavra_rev = palavra[::-1]  # reverte a palavra

    tamanho_palavra = len(palavra) #

    palindroma = ' ' # variável que recebe os caracteres repetidos (maior substring palíndroma)

    for i in range (tamanho_palavra): # loop para verificação de cada letra da string digitada
        for j in range (i + 1, tamanho_palavra + 1):
            palavra_int = palavra[i:j]
            if palavra_int == palavra_int[::-1] and len (palavra_int) > len (palindroma):
                palindroma = palavra_int

    return palindroma

palavra_original = input("Digitar a palavra: ")  # recebe a palavra digitada

palavra_nova = verif_palindroma(palavra_original)  # chama a função para verificação da maior substring palíndroma

print("A maior substring palíndroma é: ", palavra_nova) # imprime na tela a maior substring palíndroma

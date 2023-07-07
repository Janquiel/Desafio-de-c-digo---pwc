def reverter(frase):  # função para reverter a frase

    palavras = frase.split()  # divide a frase em palavras

    frase_revertida = ' '.join(palavras[::-1])  # junta as palavras novamente para formar uma frase em ondem reversa

    return frase_revertida  # retorna a frase completa revertida

frase = input("Digitar a frase: ")  # recebe a frase

frase_revertida = reverter(frase)  # chama a função para reverter a frase

print("Frase revertida: ", frase_revertida)  # imprime na tela a frase revertida

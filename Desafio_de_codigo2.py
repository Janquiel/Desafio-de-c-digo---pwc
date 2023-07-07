def remov_repet(frase): # função para verificar os caracteres repetidos
    sem_repet = " " # cria a variável sem_repet vazia, para alocar apenas os caracteres que não se repetem

    for caractere in frase: # loop para verificação dos caracteres
        if caractere not in sem_repet or caractere == " ": # se o caractere não é repetido ou é um espaço, vai para a variável sem_repet
            sem_repet += caractere # faz a iteração para verificar o próximo caractere

    return sem_repet # retorna apenas os caracteres que não são repetidos

frase = input ("Digitar a frase: ") # recebe a frase digitada

frase_nova = remov_repet(frase) # chama a função de remover os caracteres repetidos

print("Frase sem caracteres repetidos: ", frase_nova) # imprime na tela a frase sem os caracteres repetidos
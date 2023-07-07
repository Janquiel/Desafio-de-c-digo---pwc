def maiuscula(frase):  # função para colocar letra maiúscula no início do parágrafo

    palavras = frase.split('. ')  # divide a frase em palavras

    palavras = [frase.capitalize() for frase in palavras] #coloca letra maiúscula na primeira palavra depois do ponto

    frase_maiuscula = '. '.join(palavras)  # une as palavras em uma frase novamente

    return frase_maiuscula  # retorna a frase completa com as letras maiúsculas

frase_original = input("Digitar a frase: ")  # recebe a frase digitada

frase_maiuscula = maiuscula(frase_original)  # chama a função para colocar as letras maiúsculas

print("Frase com letras maiusculas no inicio do paragrafo: ", frase_maiuscula)  # imprime na tela a frase ajustada
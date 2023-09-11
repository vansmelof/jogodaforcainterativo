import random


def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


        if (nivel == 1):
            tentativas = 8
            enforcou = erros == tentativas
        elif (nivel == 2):
            tentativas = 6
            enforcou = erros == tentativas
        else:
            tentativas = 4
            enforcou = erros == tentativas

        if erros >= 1:
            print(f"Você tem {tentativas - erros} tentativas")

    if acertou:
        print("Parabéns!! Você ganhou!!!")
    else:
        print(f"Que pena. A palavra secreta era {palavra_secreta}. Você perdeu!!!")

    print("Fim do jogo!")


if (__name__ == "__main__"):
    jogar()

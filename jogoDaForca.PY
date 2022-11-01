from funcoes import limparTela

desafiante = input("Nome do desafiante: ")
jogador = input("Nome do jogador: ")

while True:
    letras = []
    letrasOcultas = []
    tentativa = []
    Dicas = 0
    erros = 0
    
    limparTela()
    palavraChave = str(input("Desafiante insira a palavra: "))
    dica1 = str(input("Dica 1: "))
    dica2 = str(input("Dica 2: "))
    dica3 = str(input("Dica 3: "))
    limparTela()

    for i in (palavraChave):
        letras.append(i)
    for x in range(len(letras)):
        letrasOcultas.append("_ ")
    print(''.join(map(str, letrasOcultas)))

    while True:  
        try:
            print ("Para jogar, digite '1'!")
            print ("Para dicas, digite '2'!")
            comando = int(input())
        except:
            print("Comando inválido")
            print ("Para jogar, digite '1'!")
            print ("Para dicas, digite '2'!")
            comando = int(input())
        limparTela()
        if comando == 1:
            print(''.join(map(str, letrasOcultas)))
            letra = str(input("Digite a sua letra: "))
            if letra in letras:
                if letra in tentativa:
                    print("Você já digitou essa letra!")
                    continue
                tentativa += letra
                print("Acertou mizeravi!")
                for i in range(len(letras)):
                    if letra == letras[i]:
                        letrasOcultas[i] = letra
                print(''.join(map(str, letrasOcultas)))
                if letras == letrasOcultas:
                    limparTela()
                    print("Parabéns! Você ganhou um belo nada!")
                    print(''.join(map(str, letrasOcultas)))
                    break
            else:
                if letra in tentativa:
                    print("Você já digitou essa letra!")
                    continue
                else:
                    tentativa += letra
                    erros +=1
                    if erros == 1:
                        print("ERoooouuu 1")
                    elif erros == 2:
                        print("Vixi tenta denovo 2")
                    elif erros == 3:
                        print("Ó a pressão 3")
                    elif erros == 4:
                        print("Ai Ai meu coração 4")  
                    elif erros == 5:
                        print("Última chance 5") 
                    else:
                        print("Perdeu rapaiz!")
                        break
                    
        if comando == 2:
            Dicas += 1
            if Dicas == 1:
                print(f"Dica 1:",dica1)
            elif Dicas == 2:
                print(f"Dica 2:",dica2)
            elif Dicas == 3:
                print(f"Dica 3:",dica3)
            else:
                print("Cabou as dicas fi, tenta a sorte agora ;)")  

    jogarNovamente = input("Se deseja jogar novamente digite '1' se deseja fechar o jogo digite '2': ")
    if jogarNovamente == '1':
        continue
    else:
        break
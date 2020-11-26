import adivinhacao
import forca



def escolhe_jogos():
    print('**************************')
    print('*****Escolha seu jogo*****')
    print('**************************')

    print('(1)Adivinhação -- (2)Forca')

    jogo = int(input('Digite o número do seu jogo: '))

    if jogo == 1:
        print('Jogando adivinhação!')
        adivinhacao.jogar()
    elif jogo == 2:
        print('Jogando forca!')
        forca.jogar()


if __name__ ==  "__main__":
    escolhe_jogos()

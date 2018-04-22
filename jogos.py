import adivinhacao
import forca

def escolhe_jogo():

    print('******************************')
    print('*** Bem vindo aos jogos!!! ***')
    print('******************************')

    print('\n(1) Forca - (2) Advinhação\n')

    jogo = int(input('Selecione o jogo que você quer jogar: '))

    while jogo < 1 or jogo > 2:
        print('Nooop\n')
        jogo = int(input('Selecione o jogo que você quer jogar: '))


    if jogo == 1:
        jogo_selecionado = 'da Forca'
        forca.jogar()

    elif jogo == 2:
        jogo_selecionado = 'de Advinhação'
        adivinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()
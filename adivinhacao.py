import random as r

def jogar():

    print('\n*********************************')
    print('Bem vindo ao jogo de adivinhação!')
    print('*********************************\n')

    numero_secreto = r.randrange(1, 100+1)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil\n")

    nivel = int(input("Defina seu nível: "))


    while nivel < 1 or nivel > 3:
        print('\nEntre 1 e 3, por favor!')
        nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    print('=========================')

    for rodada in range(1, total_tentativas + 1):
        print('\nTentativa {} de {}'.format(rodada, total_tentativas))

        chute_str = input('Chute seu número: ')
        chute = int(chute_str)

        if chute < 1 or chute >100:
            print('Você deve digitar um número entre 1 e 100')
            print('=========================================')
            continue

        igual = chute == numero_secreto
        menor = chute < numero_secreto
        maior = chute > numero_secreto

        if igual:
            print('-------------------------')
            print('Parabéns, você acertou e fez {} pontos!!!'.format(pontos))
            print('-------------------------')
            print('=========================')
            break

        else:
            if menor:
                print('Errrrrrou para menos.')
                pontos_perdidos = abs(chute - numero_secreto)
                pontos = pontos - pontos_perdidos

            else:
                print('Errrrrrou para mais.')
                pontos_perdidos = abs(chute - numero_secreto)
                pontos = pontos - pontos_perdidos

        print('====================')

    if not igual:
        print('O número secreto era {}'.format(numero_secreto))

    print('---FIM---')


if __name__ == '__main__':
    jogar()
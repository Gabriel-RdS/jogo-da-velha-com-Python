import random


def jogar():
    print('*********************************')
    print('Bem-vindo ao jogo de adivinhação!')
    print('*********************************')

    numero_secreto = random.randrange(1, 101)
    numero_tentativas = 0
    pontos = 1000

    print('Defina um nível!')
    print('Fácil(1)--Médio(2)--Difícil(3)')

    nivel = int(input('Digite o nível entre 1 e 3: '))

    if nivel == 1:
        numero_tentativas = 15
        print('Você escolheu nível: Fácil')
        print('---------------------------------------------')
    elif nivel == 2:
        numero_tentativas = 10
        print('Você escolheu nível: Médio')
        print('---------------------------------------------')
    elif nivel == 3:
        numero_tentativas = 5
        print('Você escolheu nível: Difícil')
        print('---------------------------------------------')

    for rodada in range(1, numero_tentativas + 1):
        print(f'Rodada {rodada} de {numero_tentativas}')
        chute = int(input("Digite um número entre 1 e 100: "))
        print('---------------------------------------------')
        print(f'Você digitou: {chute}')

        if chute > 100 or chute < 1:
            print('Você deve chutar um número entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        menor = chute < numero_secreto
        maior = chute > numero_secreto

        if acertou:
            print('Você acertou!')
            break
        else:
            if menor:
                print('Você chutou um número menor!')
            elif maior:
                print('Você chutou um número maior!')
            pontos_perdidos = abs(numero_secreto + chute)
            pontos = pontos - pontos_perdidos

    print(f'O número secreto é: {numero_secreto}')
    print(f'Sua pontuação é igual: {pontos}')
    print('Fim de jogo!')

if __name__ == "__main__":
    jogar()

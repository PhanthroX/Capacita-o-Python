import random

def gerar_numero_aleatorio():
    numero_aleatorio = random.randint(0, 100)
    return numero_aleatorio

def avaliar_numero(numero_aleatorio):
    numero_digitado = int(input("Digite um número: "))

    if numero_digitado == numero_aleatorio:
        return 0
    elif numero_digitado < numero_aleatorio:
        return -1
    else:
        return 1

def jogo_adivinhacao():
    numero_aleatorio = gerar_numero_aleatorio()
    tentativas = 10

    while tentativas > 0:
        resultado = avaliar_numero(numero_aleatorio)

        if resultado == 0:
            print("Parabéns! Você acertou o número!")
            return
        elif resultado == -1:
            print("O número digitado é menor que o número sorteado.")
        else:
            print("O número digitado é maior que o número sorteado.")

        tentativas -= 1
        print("Tentativas restantes:", tentativas)

    print("Você perdeu! O número sorteado era:", numero_aleatorio)

jogo_adivinhacao()
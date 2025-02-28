import random


print("### MENU DE DIFICULDADE ###")
print("1 - Fácil (1 a 50, 5 tentativas)")
print("2 - Médio (1 a 100, 4 tentativas)")
print("3 - Difícil (1 a 200, 3 tentativas)")


opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    numero_max = 50
    tentativas_max = 5
    print("Você escolheu a dificuldade Fácil!")
elif opcao == 2:
    numero_max = 100
    tentativas_max = 4
    print("Você escolheu a dificuldade Média!")
elif opcao == 3:
    numero_max = 200
    tentativas_max = 3
    print("Você escolheu a dificuldade Difícil!")
else:
    print("Opção inválida!")
    exit()  


sorteio = random.randint(1, numero_max)


print("Adivinhe o número que estou pensando, de 1 a", numero_max)
tentativas = 1


while tentativas <= tentativas_max:
    print("Tentativa ",tentativas)
    chute = int(input("Digite o seu chute: "))

    if chute == sorteio:
        print("Parabéns, você acertou! O número era ",sorteio)
        break
    elif chute > sorteio:
        print("Chute um número menor.")
    else:
        print("Chute um número maior.")

    tentativas += 1

if chute != sorteio:
    print("Você não acertou. O número era, sorteio.")
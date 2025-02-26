import random
sorteio = random.randint(1, 10)
print(sorteio)

numero_max = 10
limite_tentativas = 5

sorteio = random.randint(1, numero_max)
#print(sorteio)
print("### JOGO DA ADIVINHAÇÃO ###")
print("Adivinhe o número que estou pensando, de 1 a 10")
limite_tentativas = 3
tentativa = 1
while (limite_tentativas >= tentativa):
    print("Tentativa", tentativa)
@@ -16,3 +19,7 @@
    elif (chute < sorteio):
        print("Chute um número maior!")
    tentativa = tentativa + 1
    # FINAL DO LAÇO WHILE
print("O número sorteado era: ##", sorteio, "##")
print("### FIM DO JOGO ###")

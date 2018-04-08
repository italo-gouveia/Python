import random

guessNumber = random.randint(0, 100)
inf = 0
sup = 100
venceu = False
tentativas = 0


while(venceu == False):
    print('Digite um número entre', inf, ' e ', sup)
    palpite = int(input())

    if palpite == guessNumber:
        print('Parabéns, você venceu!')
        tentativas += 1
        venceu = True
    if palpite < guessNumber:
        inf = palpite
        tentativas += 1
    if palpite > guessNumber:
        sup = palpite
        tentativas += 1

print("Quantidade de tentativas", tentativas);
print("Fim do programa");
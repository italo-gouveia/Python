av1 = input("Digite a primeira nota")
av2 = input("Digite a segunda nota")
av3 = input("Digite a terceira nota")
media = (float(av1)+float(av2)+float(av3))/3

if media >= 6:
    print("Aluno aprovado com média: ", media)
elif media < 6 and media > 3.9:
    print("Aluno irá fazer AVR")
elif media <= 3.9:
    print("Aluno reprovado com média: ", media)
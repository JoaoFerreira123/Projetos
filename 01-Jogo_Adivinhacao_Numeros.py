""""
Construa um jogo de adivinhação de números, no qual o usuário seleciona um intervalo.
Digamos que o usuário tenha selecionado um intervalo, ou seja, de A a B , onde A e B pertencem a inteiro.
Algum inteiro aleatório será selecionado pelo sistema e o usuário deve adivinhar esse inteiro no número mínimo de adivinhações
"""

from random import randint

print("=-"*20)
print("Bem Vindo ao Jogo de Adivinhação")
print("=-"*20)
min = int(input("Insira o início do intervalo: "))
max = int(input('Insira o final do intervalo: '))
print('=-'*20)
num = randint(min, max)
cont = 0

while True:
    player = int(input('Qual o seu palpite? '))
    if player > num:
        print('Muito alto... Tente um número mais baixo')
        cont+=1        
    elif player < num:
        print('Muito baixo... Tente um número mais alto')
        cont+=1

    else:
        print(f'PARABÉNS, você acertou com {cont+1} tentativas!!\nO número sorteado foi: {num}')
        break

    

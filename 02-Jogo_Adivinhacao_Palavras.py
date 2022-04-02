""""
Neste jogo, há uma lista de palavras presentes, da qual nosso intérprete escolherá 1 palavra aleatória. 
O usuário primeiro deve inserir seus nomes e, em seguida, será solicitado a adivinhar qualquer alfabeto.
Se a palavra aleatória contiver esse alfabeto, ela será mostrada como saída (com o posicionamento correto). 
caso contrário, o programa solicitará que você adivinhe outro alfabeto.
O usuário terá 12 chances (pode ser alterado de acordo) para adivinhar a palavra completa.
"""


from random import choice
from re import I

palavras = ['engrenagem', 'motor',  'arduino', 'ESP23', 'resistor', 'circuito', 'alavanca', 'mecanismo']
print('=-'*20)
print('Bem Vindo ao Adivinhe Engenheiro')
print('=-'*20)
print('Tente adivinhar palavras de *ENGENHARIA*')
print()

palavra = choice(palavras)

#para que as letras que já foram acertadas continuem aparecendo, basta criar uma lista com traços e
#se acertar, altera de traços pra letra, e daí continua mostrando a lista
tam = len(palavra)
p_oculta = ['-'] * tam 
pontos = tam+2
print(f'Vamos começar... Você tem {pontos} chances para acertar')

while True:
    letra = input('Qual seu  palpite? ')
    for i in range(tam):
        if palavra[i] == letra:
            p_oculta[i] = letra
    print(''.join(p_oculta))
    pontos-=1
    print(f'Você ainda tem {pontos} chances')
    if pontos == 0:
        print('Você Perdeu!')
        break
    if ''.join(p_oculta) == palavra:
        print('Você ganhou!!')
        break
    

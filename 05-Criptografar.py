#//Crie um algoritmo de programação que, para cada vogal digitada de uma palavra, ele substitua a vogal por uma palavra
#Quero fazer com o alfabeto completo! Com a primeira letra da palavra "verdadeira" correspondendo a primeira letra da palavra criptografada
#OU algum outro tipo de lógica para que tenha alguma letra da palavra verdadeira na palavra criptografada
#Alguma senha pra indicar a posição da letra?? sla PENSAR SOBRE!!!!


palavras = list()

palavras = ['abacaxi', 'elefante', 'india', 'outubro', 'urubu']
texto = input('DIgite o texto: ').lower()
cripto = list()

def criptografar(texto):

    for i in texto:
        if i == 'a':
            cripto.append(palavras[0])
        if i == 'e':
            cripto.append(palavras[1])
        if i == 'i':
            cripto.append(palavras[2])
        if i == 'o':
            cripto.append(palavras[3])
        if i == 'u':
            cripto.append(palavras[4])

    return(cripto)

print(criptografar(texto))

def descriptografar(cripto):
    pal = list()
    for i in cripto:
        if i == palavras[0]:
            pal.append('a')
        if i == palavras[1]:
            pal.append('e')
        if i == palavras[2]:
            pal.append('i')
        if i == palavras[3]:
            pal.append('o')
        if i == palavras[4]:
            pal.append('u')
    return(pal)

print(descriptografar(cripto))
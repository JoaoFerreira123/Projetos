from random import choice

caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789*!@#$%&'

n_senhas = int(input('Quantas senhas você deseja? '))
tam_senhas = int(input('Qual o tamanho das senhas? '))

for i in range(0, n_senhas):
    senha = ''
    for j in range(0, tam_senhas):
        senha += choice(caracteres) #adiciona caracteres aleatórios na string
    print(senha)
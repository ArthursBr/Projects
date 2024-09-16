from random import randint
from time import sleep
c = randint(1, 3)
j = int(input('''Suas opções:
      [ 1 ] PEDRA
      [ 2 ] PAPEL
      [ 3 ] TESOURA
Qual a sua jogada: '''))
sleep(2)
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO!!!')
print('-=-=' * 7)

# cj
if c == 1:
    cj = ('Pedra')
elif c == 2:
    cj = ('Papel')
else:
    cj = ('Tesoura')

# jj
if j == 1:
    jj = ('Pedra')
elif j == 2:
    jj = ('Papel')
elif j == 3:
    jj = ('Tesoura')
else:
    jj = ('       ')

print('''Computador jogou {}
      Jogador jogou {}'''.format(cj, jj))

print('-=-=' * 7)
if j != 1 and j != 2 and j != 3:
    print('JOGADOR NÃO JOGOU')
elif c == j:
    print('EMPATE')
elif c == 1 and j == 2 or c == 2 and j == 3 or c == 3 and j == 1:
    print('JOGADOR VENCE')
elif j == 1 and c == 2 or j == 2 and c == 3 or j == 3 and c == 1:
    print('COMPUTADOR VENCE')

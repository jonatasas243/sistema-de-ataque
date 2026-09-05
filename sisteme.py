import random
from class1 import jogador,inimigo,ataque_heroi,ataque_inimigo
print('='*60)
print('bem vindo ao jogo de batalha')
print('='*60)

###ATAQUES DO HEROI###
FOGO = ataque_heroi('fogo',50)
AGUA = ataque_heroi('agua',30)
TERRA = ataque_heroi('terra',70)

###ATAQUES DO INIMIGO###
FURIA = ataque_inimigo('furia',50)
nulo = ataque_inimigo('nulo',0)
pedra = ataque_inimigo('pedra',30)

a = input('voce quer jogar? [s/n]: ')

if a == 's' or a == 'sim':
    print('bem vindo ao jogo')
    jogador = jogador()
    inimigo = inimigo()
    while jogador.vida > 0 and inimigo.vida > 0:
        print('escolha seu ataque')
        print('1 - fogo')
        print('2 - agua')
        print('3 - terra')
        escolha = input('qual ataque voce quer usar? ')
        if escolha in ['1','fogo']:
            FOGO.usar(inimigo)
        elif escolha in ['2','agua']:
            AGUA.usar(inimigo)
        elif escolha in ['3','terra']:
            TERRA.usar(inimigo)
        else:
            print('opção invalida')

        ataque_inimigo = random.choice([FURIA,nulo,pedra])
        ataque_inimigo.usar(jogador)
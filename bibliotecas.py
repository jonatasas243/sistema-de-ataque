class jogador:
    def __init__(self,vida = 1000):
        self.vida = vida


    def receber_dano(self,dano):
        self.vida -= dano
        print(f"sua vida atual é {self.vida}")
        if self.vida <= 0 :
            print(f'sua vida chegou a {self.vida}e voce fo derrotado')


class ataque:
    def __init__(self,nome,dano):
        self.dano = dano
        self.nome = nome

    def usar(self,alvo:jogador):
        print(f'vpoder de {self.nome}haaaaaaaaaa \n vc causou{self.dano} de dano')
        alvo.receber_dano(self.dano)


fogo = ataque('fogo',50)
agua = ataque('agua',30)
terra = ataque('terra',70)

print('='*50)
print('SISTEMA DE JOGO')
print('='*50)
a = input('voce quer jogar? [s/n]: ')

if a == 's' or a == 'sim':
    print('bem vindo ao jogo')
    jogador = jogador()
    while jogador.vida > 0:
        print('escolha seu ataque')
        print('1 - fogo')
        print('2 - agua')
        print('3 - terra')
        escolha = input('qual ataque voce quer usar? ')
        if escolha in ['1','fogo']:
            fogo.usar(jogador)
        elif escolha in ['2','agua']:
            agua.usar(jogador)
        elif escolha in ['3','terra']:
            terra.usar(jogador)
        else:
            print('opção invalida')
else:
    print('ok, ate a proxima')
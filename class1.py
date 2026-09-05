class jogador:
    def __init__(self,vida = 500):
        self.vida = vida


    def receber_dano(self,dano):
        self.vida -= dano
        print(f"sua vida atual do heroi é {self.vida}")
        if self.vida <= 0 :
            print(f'a vida do heroi chegou a {self.vida} e o heroi foi derrotado')
class inimigo:
    def __init__(self,vida = 1000):
        self.vida = vida


    def receber_dano(self,dano):
        self.vida -= dano
        print(f"vida do inimigo {self.vida}")
        if self.vida <= 0 :
            print(f'a vida do inimigo chegou a {self.vida} e o heroi foi derrotado')

class ataque_heroi:
    def __init__(self,nome,dano):
        self.dano = dano
        self.nome = nome

    def usar(self,alvo:inimigo):
        print(f'poder de {self.nome} haaaaaaaaaaa razenga \n vc causou {self.dano} de dano')
        alvo.receber_dano(self.dano)

class ataque_inimigo:
    def __init__(self,nome,dano):
        self.dano = dano
        self.nome = nome

    def usar(self,alvo:jogador):
        print(f'poder de {self.nome} haaaaaaaaaaa razenga \n o inimigo causou {self.dano} de dano')
        alvo.receber_dano(self.dano)


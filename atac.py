vida = 100
print('='*50)
print('SISTEMA DE ATAQUE')
print('='*50)
a = input('voce que continua: sim ou nao\n').strip().lower()

def atac():
    global vida
    a = input('1 fogo , 2 agua ,3 terra\n').strip().lower()
    if a == '1' or a == 'fogo':
        print('poder de fogo haaaaaaaaaaaaaaaaaaa \n(poder de fogo 30 de dano)')
        
        vida -= 30
        print(f"sua vida atual é {vida}")
    elif a == '2' or a == 'agua':
        print('poder de agua haaaaaaaaaaaaaaaaaa \n (poder de agua 20 de dano)')
        
        vida -= 20
        print(f'sua vida atual é {vida}')
    elif a == '3' or a == 'terra':
        print('poder de terra haaaaaaaaaaaaaaaaaa \n (poder de terra 70 de dano)')
        
        vida -= 70
        print(f'sua vida atual é {vida}')
    else:
        print('ta na minha maldade pai ')

if a == 'sim':
    while vida > 0:
        atac()
elif a == 'nao':
    print('ok')
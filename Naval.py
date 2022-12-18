import random

player = []
inimigo = []
InimigoEscondido = []

for x in range(5):
    player.append(["0"] * 5)
for y in range(5):
    inimigo.append(["0"] * 5)
for z in range(5):
    InimigoEscondido.append(["0"] * 5)



def Tabuleiro(player):
    print("Batalha Naval")
    print('  0 1 2 3 4')
    l=0

    for linha in player:
        print("%d|%s|" % (l," ".join(linha)))
        l += 1



def navioPlayer():
    print(f"Posicione nossos 5 Navios Capitão!")
    for i in range(5):
        linhaPlayer = int(input("escolha a linha: "))

        while linhaPlayer not in(0, 1, 2, 3, 4):
            print("Esse não Capitão...")
            linhaPlayer = int(input("escolha a linha: "))

        colunaPlayer = int(input("escolha a coluna: "))

        while colunaPlayer not in (0, 1, 2, 3, 4):
            print("Esse não Capitão...")
            colunaPlayer = int(input("escolha uma coluna: "))
        
        player[linhaPlayer][colunaPlayer] = '\33[7;49;34mN\033[m'
        return int(linhaPlayer), int(colunaPlayer)


def navioInimigo(inimigo):
    for j in range(5):
        linhaInimigo = int(random.randint(0,4))
        colunaInimigo = int(random.randint(0,4))

        while inimigo[linhaInimigo][colunaInimigo] == '\33[7;49;34mN\033[m':
            linhaInimigo = int(random.randint(0,4))
            colunaInimigo = int(random.randint(0,4))

        inimigo[linhaInimigo][colunaInimigo] = '\33[7;49;34mN\033[m'
        return int(linhaInimigo), int(colunaInimigo)


def tiro():
    linhatiro = int(input("linha: "))
    while linhatiro not in (0, 1, 2, 3, 4):
        print("Esse não Capitão...")
        linhatiro = int(input("linha: "))

    colunatiro = int(input("coluna: "))
    while colunatiro not in (0, 1, 2, 3, 4):
        print("Esse não Capitão...")
        colunatiro = int(input("coluna: "))

    return int(linhatiro), int(colunatiro)


def tiroIA():
    linhatiroInimigo = int(random.randint(0,4))
    colunatiroInimigo = int(random.randint(0,4))

    while player[linhatiroInimigo][colunatiroInimigo] == '\33[7;49;32mX\033[m' or player[linhatiroInimigo][colunatiroInimigo] == '\33[7;49;31m0\033[m':
        linhatiroInimigo = int(random.randint(0,4))
        colunatiroInimigo = int(random.randint(0,4))

    return linhatiroInimigo, colunatiroInimigo


Tabuleiro(player)
navios = 5 
while navios != 0:
    linhaPlayer, colunaPlayer = navioPlayer()
    navioInimigo(inimigo)
    Tabuleiro(player)
    navios -= 1


print('Preparar para a Batalha Capitão!')
c = 0
c1 = 0
n = 5
n1 = 5
while True:
    print("   Você")
    Tabuleiro(player)
    print('  Inimigo')
    Tabuleiro(InimigoEscondido)
    print('   Placar')
    print(f"você:{c} inimigo:{c1}")
    print(f"Seus navios:{n1} Navios inimigos:{n}")
    linhatiro,colunatiro = tiro()
    if InimigoEscondido[linhatiro][colunatiro] == '\33[7;49;31mO\033[m':
        print("-" * 30)
        print("Você já mirou ai Capitão!")
        print("-" * 30)
    else:
        if InimigoEscondido[linhatiro][colunatiro] == '\33[7;49;32mX\033[m':
            print("-" * 30)
            print("Você já afundou esse Navio Capitão!")
            print("-" * 30)
        else:
            if inimigo[linhatiro][colunatiro] =='\33[7;49;34mN\033[m':
                print("-" * 30)
                print("Acertou em cheio Capitão!")
                print("-" * 30)
                InimigoEscondido[linhatiro][colunatiro] = '\33[7;49;32mX\033[m'
                c += 1
                n -= 1
            else:
                print("-" * 30)
                print("Acertamos só agua Capitão!")
                print("-" * 30)
                InimigoEscondido[linhatiro][colunatiro] = '\33[7;49;31mO\033[m'
    if c == 5:
        print("-" * 30)
        print("Parabéns Capitão, destruimos todos os navios inimigos!")
        print("-" * 30)
        break
    print("O inimigo está atirando capitão!")
    linhatiroInimigo, colunatiroInimigo = tiroIA()
    if player[linhatiroInimigo][colunatiroInimigo] == '\33[7;49;34mN\033[m':
        print(f"O inimigo atirou nas coordenadas ({linhatiroInimigo}:{colunatiroInimigo}) Capitão!")
        print("O inimigo acertou um dos nossos Capitão!")
        print("-" * 30)
        player[linhatiroInimigo][colunatiroInimigo] = '\33[7;49;32mX\033[m'
        c1 += 1
        n1 -= 1
    else:
        print(f"O inimigo atirou nas coordenadas ({linhatiroInimigo}:{colunatiroInimigo}) Capitão!")
        print("O inimigo atirou na água Capitão!")
        print("-" * 30)
        player[linhatiroInimigo][colunatiroInimigo] = '\33[7;49;31mO\033[m'
    if c1 == 5:
        print("-" * 30)
        print("Perdemos toda nossa frota capitão, fomos derrotados...")
        print("-" * 30)
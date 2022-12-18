import random

Player = []
IA = []
IAescondida = []

for x in range(5):
    Player.append(["0"] * 5)
for y in range(5):
    IA.append(["0"] * 5)
for z in range(5):
    IAescondida.append(["0"] * 5)



def Tabuleiro(Player):
    print("Batalha Naval")
    print('  0 1 2 3 4')
    l=0
    for linha in Player:
        print("%d|%s|" % (l," ".join(linha)))
        l += 1



def NavioPlayer():
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
        
        Player[linhaPlayer][colunaPlayer] = '\33[7;49;34mN\033[m'
        return int(linhaPlayer), int(colunaPlayer)
        
def NavioIA(IA):
    for j in range(5):
        linhaIA = int(random.randint(0,4))
        colunaIA = int(random.randint(0,4))
        while IA[linhaIA][colunaIA] == '\33[7;49;34mN\033[m':
            linhaIA = int(random.randint(0,4))
            colunaIA = int(random.randint(0,4))
        IA[linhaIA][colunaIA] = '\33[7;49;34mN\033[m'
        return int(linhaIA), int(colunaIA)

def tiro():
    linhatiro = int(input("linha: "))
    while linhatiro not in (0, 1, 2, 3, 4):
        print("Esse não Capitão...")
        linhatiro = int(input("linha: "))
    colunatiro = int(input("coluna: "))
    while colunatiro not in (0, 1, 2, 3, 4):
        print("Esse não Capitão...")
        colunatiro = int(input("coluna: "))
    return int(linhatiro),int(colunatiro)

def tiroIA():
    linhatiroIA = int(random.randint(0,4))
    colunatiroIA = int(random.randint(0,4))

    while Player[linhatiroIA][colunatiroIA] == '\33[7;49;32mX\033[m' or Player[linhatiroIA][colunatiroIA] == '\33[7;49;34m0\033[m':
        linhatiroIA = int(random.randint(0,4))
        colunatiroIA = int(random.randint(0,4))
    return linhatiroIA, colunatiroIA

Tabuleiro(Player)
navios = 5 
while navios!=0:
    linhaPlayer, colunaPlayer = NavioPlayer()
    NavioIA(IA)
    Tabuleiro(Player)
    navios -= 1

print('Preparar para a Batalha Capitão!')
c = 0
c1 = 0
n = 5
n1 = 5
while True:
    print("Você")
    Tabuleiro(Player)
    print('Inimigo')
    Tabuleiro(IAescondida)
    print('Placar')
    print(f"você:{c} inimigo:{c1}")
    print(f"Seus navios:{n1} Navios inimigos:{n}")
    linhatiro,colunatiro = tiro()
    if IAescondida[linhatiro][colunatiro] == '\33[7;49;31mO\033[m':
        print("-" * 30)
        print("Você já mirou ai Capitão!")
        print("-" * 30)
    else:
        if IAescondida[linhatiro][colunatiro] == '\33[7;49;32mX\033[m':
            print("-" * 30)
            print("Você já afundou esse Navio Capitão!")
            print("-" * 30)
        else:
            if IA[linhatiro][colunatiro] =='\33[7;49;34mN\033[m':
                print("-" * 30)
                print("Acertou em cheio Capitão!")
                print("-" * 30)
                IAescondida[linhatiro][colunatiro] == '\33[7;49;34mN\033[m'
                c += 1
                n -= 1
            else:
                print("-" * 30)
                print("Acertamos só agua Capitão!")
                print("-" * 30)
                IAescondida[linhatiro][colunatiro] = '\33[7;49;31mO\033[m'
    if c == 5:
        print("-" * 30)
        print("Parabéns Capitão, destruimos todos os navios inimigos!")
        print("-" * 30)
        break
    print("O inimigo está atirando capitão!")
    linhatiroIA, colunatiroIA = tiroIA()
    if Player[linhatiroIA][colunatiroIA] == '\33[7;49;34mN\033[m':
        print(f"O inimigo atirou nas coordenadas ({linhatiroIA}:{colunatiroIA}) Capitão!")
        print("O Inimigo acertou um dos nossos Capitão!")
        print("-" * 30)
    else:
        Player[linhatiroIA][colunatiroIA] == '\33[7;49;32mX\033[m'
        print(f"O inimigo atirou nas coordenadas ({linhatiroIA}:{colunatiroIA}) Capitão!")
        print("O Inimigo atirou na água Capitão!")
        print("-" * 30)

    if c1 == 5:
        print("-" * 30)
        print("Perdemos toda nossa frota capitão, fomos derrotados...")
        print("-" * 30)
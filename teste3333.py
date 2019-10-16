import random, os

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

def pula_linha():
    print('')

def printa_carteira():
    print(f'A carteira de {nome} é {dic_players_carteira[nome]}')

def printa_cartas():
    print(f'{nome},\nSuas cartas são: {dic_players_cartas[nome]}, Total = [{calcula_mao(dic_players_cartas[nome])}]')

def calcula_mao(mao):
    soma = 0

    nao_as = [carta for carta in mao if carta != 'A']
    as_ = [carta for carta in mao if carta == 'A']

    for carta in nao_as:
        if carta in 'JQK':
            soma += 10 
        else:
            soma += int(carta)

    for carta in as_:
        if soma <= 10:
            soma += 11
        else:
            soma += 1

    return soma

limpa()

lista_b = [
    'A','2','3','4','5','6','7','8','9','10','J','Q','K',
    'A','2','3','4','5','6','7','8','9','10','J','Q','K',
    'A','2','3','4','5','6','7','8','9','10','J','Q','K',
    'A','2','3','4','5','6','7','8','9','10','J','Q','K'
]
quer_jogar = True

while quer_jogar == True:

    snum_p = input('Quantas pessoas vão jogar? ')
    num_p = int(snum_p)
    contador_p = 0
    players = []

    while contador_p < num_p:
        players.append(input(f'Jogador[{contador_p+1}], digite seu nome:\n... ').upper())
        contador_p+= 1

    limpa()

    baralho = lista_b
    random.shuffle(baralho)

    dic_players_cartas = {}
    dic_players_carteira = {}
    dic_players_score = {}
    dic_players_carteira = {}
    cartas_croupier = []




    for nome in players:
        lista_cartas = []
        lista_cartas.append(baralho.pop())
        lista_cartas.append(baralho.pop())    
        dic_players_cartas[nome] = lista_cartas
        dic_players_carteira[nome] = 100

    cartas_croupier.append(baralho.pop())
    cartas_croupier.append(baralho.pop())
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
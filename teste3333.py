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

    lista_calcula_mao = []
    #cartas

    print('Com quantos baralhos vocês querem jogar?')
    snum_b = input('Digite entre 1 e 5: ')
    while snum_b not in ['1', '2', '3', '4', '5']:
        snum_b = input('Valor inválido!\nDigite um valor entre 1 e 5: ')
    num_b = int(snum_b)
    baralho = num_b*lista_b

    limpa()



    for nome in dic_players_cartas:
        #lista_cartas = [dic_players_cartas[nome]]
        cont = 1 
        cont_c = 1
        while cont_c != 0:
            printa_carteira()
            pula_linha
            print(f'{nome},\nQuanto você quer apostar?')
            sv_aposta = input('... ')
            v_aposta = int(sv_aposta)
            dic_players_carteira[nome] -= v_aposta
            printa_carteira()
            cont_c = 0
            
        while cont != 0:
            if dic_players_carteira[nome] >= 0:
                printa_cartas()
                print(f'As cartas do croupier [{cartas_croupier[0]}][?]')            
                print('\n[1] para mais uma carta.\n[2] para parar.')
                
                escolha = input('Escolha: ')
                pula_linha()
                if escolha == '1':
                    #lista_cartas.append(baralho.pop())
                    dic_players_cartas[nome].append(baralho.pop())
                if escolha == '2':
                    print('Fim do turno!')
                    pula_linha()
                    cont = 0
                
                if calcula_mao(dic_players_cartas[nome]) == 21:
                    print(f'{nome},\nSuas cartas são: {dic_players_cartas[nome]}, Total = [{calcula_mao(dic_players_cartas[nome])}]')
                    pula_linha()
                    print('Fim do turno!')
                    pula_linha()
                    cont = 0
                elif calcula_mao(dic_players_cartas[nome]) > 21:
                    print(f'{nome},\nSuas cartas são: {dic_players_cartas[nome]}, Total = [{calcula_mao(dic_players_cartas[nome])}]')
                    pula_linha()
                    print('Fim do turno!')
                    pula_linha()
                    cont = 0
            else: 
                printa_carteira()
                break


import random, os, time

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

def pula_linha():
    print('')

def printa_carteira():
    print(f'A carteira de {nome.upper()} é {dic_players_carteira[nome]}')
    print('')

def printa_carteira_sn():
    print(f'Sua carteira: [{dic_players_carteira[nome]}]')
    print('')

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
rodada = 1


while quer_jogar == True:
    limpa()
    cartas_croupier = []
    baralho = lista_b
    random.shuffle(baralho)  
    dic_players_cartas = {}
    dic_players_score = {}  
    dic_verifica_primeiramao = {}    


    if rodada == 1:
        snum_p = input('Quantas pessoas vão jogar? ')
        num_p = int(snum_p)
        contador_p = 0
        players = []
        dic_players_carteira = {}

        while contador_p < num_p:
            players.append(input(f'Jogador[{contador_p+1}], digite seu nome:\n... '))
            contador_p+= 1

        for nome in players:
            dic_players_carteira[nome] = 100
        limpa()
        print('Com quantos baralhos vocês querem jogar?')
        snum_b = input('Digite entre 1 e 5: ')
        while snum_b not in ['1', '2', '3', '4', '5']:
            snum_b = input('Valor inválido!\nDigite um valor entre 1 e 5: ')
        num_b = int(snum_b)
        baralho = num_b*lista_b        
        
        rodada += 1
    

    limpa()


    for nome in players:
        lista_cartas = []
        lista_cartas.append(baralho.pop())
        lista_cartas.append(baralho.pop())    
        dic_players_cartas[nome] = lista_cartas
        dic_verifica_primeiramao[nome] = 0

    print(dic_verifica_primeiramao)

    cartas_croupier.append(baralho.pop())
    cartas_croupier.append(baralho.pop())

    lista_calcula_mao = []
    #cartas

    limpa()



    for nome in dic_players_cartas:
        cont = 1 
        cont_c = 1
        condicao_jogar = 1

        while cont_c != 0:
            if dic_players_carteira[nome] == 0:
                condicao_jogar = 0
                cont_c = 0
                
            elif dic_players_carteira[nome] >= 0:
                printa_carteira()
                pula_linha()
                print(f'{nome},\nQuanto você quer apostar?')
                v_aposta = int(input('... '))
                while v_aposta <= 0 or v_aposta > dic_players_carteira[nome]:
                    print('Valor invalido!')
                    v_aposta = int(input('Digite novamente\n.. '))
         
                dic_players_carteira[nome] -= v_aposta
                limpa()
                printa_carteira()
                cont_c = 0

        primeira_mao = True    

        while cont != 0:
            if condicao_jogar == 1:
                if primeira_mao and calcula_mao(dic_players_cartas[nome]) == 21:
                    print('Fim do turno!')
                    dic_verifica_primeiramao[nome] = 1
                    cont = 0 
                    
                primeira_mao = False                        
                

                printa_cartas()
                print(f'As cartas do croupier [{cartas_croupier[0]}][?]')
                pula_linha           
                print('\n[1] para mais uma carta.\n[2] para parar.')
                pula_linha
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
                cont = 0
                continue
        
        for i in '.........':
            time.sleep(.25)
            print(i)
        limpa()    

    for nome in dic_players_cartas:
        a = (dic_players_cartas[nome])
        dic_players_score[nome] = calcula_mao(a)

        #lista_calcula_mao.append(score)
    jj = calcula_mao(cartas_croupier)

    while jj <= 17:
            cartas_croupier.append(baralho.pop())
            jj = calcula_mao(cartas_croupier)


    print(f'As cartas do croupier foram {cartas_croupier} Total: [{calcula_mao(cartas_croupier)}]\n')
    for nome in dic_players_score:
        ps = dic_players_score[nome]
<<<<<<< HEAD
        
=======
>>>>>>> 0864544cdf7133dc29596d98d4eb2cf59962ea65
        if dic_players_carteira[nome] > 0:
            if dic_verifica_primeiramao[nome] == 1:
                print(f'{nome} GANHOU COM BLACKJACK!')
                printa_cartas()
                dic_players_carteira[nome] += v_aposta*2.5
                printa_carteira_sn()
                pula_linha()
            else:
                if ps > jj and ps <= 21:
                    print(f'{nome} GANHOU!')
                    printa_cartas()
                    dic_players_carteira[nome] += v_aposta*2
                    printa_carteira_sn()
                    pula_linha()
                elif ps > 21:
                    printa_cartas()
                    print(f'{nome} ESTOUROU!')
                    printa_carteira_sn()
                    pula_linha()       
                elif ps <=21 and jj > 21:
                    printa_cartas()
                    print(f'{nome} GANHOU, Croupier estourou!')
                    dic_players_carteira[nome] += v_aposta*2
                    printa_carteira_sn()
                    pula_linha()
                elif ps == jj:
                    printa_cartas()
                    print(f'{nome} EMPATOU')
                    dic_players_carteira[nome] += v_aposta
                    printa_carteira_sn()
                    pula_linha()        
                else:
                    printa_cartas()
                    print(f'{nome} PERDEU!')
                    printa_carteira_sn()
                    pula_linha()    

    v_resolve = False

    for nome in dic_players_carteira:
        if dic_players_carteira[nome] > 0:
            v_resolve = True
    
    if v_resolve == False:
<<<<<<< HEAD
        limpa()
        print('Todo mundo perdeu! HAHHA')
=======
        print("Todo mundo perdeu! HAHAHH")
>>>>>>> 0864544cdf7133dc29596d98d4eb2cf59962ea65
        break

    print('Quer jogar mais uma vez?')
    respostinha = input('Digite [sim] para mais uma.\nDigite [fim] para encerrar\n.. ')
    if respostinha == "sim":
        continue 
    elif respostinha == "fim":
        break

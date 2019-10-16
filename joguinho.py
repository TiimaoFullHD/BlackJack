import random, os

#funçoes 

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')


def printa_carteira():
    print(f'Carteira: {carteira}')
    
        
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

lista_b = [
    'A','2','3','4','5','6','7','8','9','10','J','Q','K',
    'A','2','3','4','5','6','7','8','9','10','J','Q','K',
    'A','2','3','4','5','6','7','8','9','10','J','Q','K',
    'A','2','3','4','5','6','7','8','9','10','J','Q','K'
]

rodada = 1

carteira = 100

limpa()
valor_aposta = 0

#entrega cartas
parar = False
primeira_mao = True


print('BEM VINDO AO CASSINSPER!')
print('')



while carteira > 0: 

    print('Você quer jogar?')
    print('')
    print('[1] para sim.')
    print('[2] para sair.')

    sjogar_sair = input('Escolha: ')
    while sjogar_sair != "1" and sjogar_sair != "2":
        print("Valor inválido")
        sjogar_sair = input('Escolha: ')

    jogar_sair = int(sjogar_sair)
    print('')

    while jogar_sair != 1 and jogar_sair!= 2:
        limpa()
        jogar_sair = int(input('Valor inválido!\n\nEscolha:\n[1] para jogar\n[2] para sair'))

    if jogar_sair == 1:
        print('')
    else: break

    limpa()

    if rodada == 1:
        print('Com quantos baralhos você quer jogar?')
        snum_b = input('Digite entre 1 e 5: ')
        while snum_b not in ['1', '2', '3', '4', '5']:
            snum_b = input('Valor inválido!\nDigite um valor entre 1 e 5: ')
        num_b = int(snum_b)
        baralho = num_b*lista_b
        rodada += 1

    limpa()
  
    parar = False
    primeira_mao = True
    
    printa_carteira()
    print('')
    valor_aposta = float(input('Digite o valor da aposta: '))
    
    while valor_aposta > carteira or valor_aposta <= 0:
        print('Valor inválido')
        valor_aposta = float(input('Digite o valor da aposta: '))
    
    #valor_aposta = svalor_aposta

    carteira -= valor_aposta

    print(f'Você apostou {valor_aposta}, e agora tem {carteira} na carteira')  

    random.shuffle(baralho)

    croupier = []

    jogador = []


    jogador.append(baralho.pop())
    croupier.append(baralho.pop())
    jogador.append(baralho.pop())
    croupier.append(baralho.pop())

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        score_jogador = calcula_mao(jogador)
        score_croupier = calcula_mao(croupier)



        if parar:
            printa_carteira()
            print(f'Aposta   = {valor_aposta}')
            print('')
            print('Cartas do croupier: [{}] [{}] '.format(']['.join(croupier), score_croupier))
            print('Suas cartas:        [{}], Total = [{}] '.format(']['.join(jogador), score_jogador))
        else:
            printa_carteira()
            print(f'Aposta   = {valor_aposta}')
            print('')
            print(f'Cartas do croupier: [{croupier[0]}] [?]')
            print('Suas cartas:        [{}], Total = [{}] '.format(']['.join(jogador), score_jogador))
            print('')

        if parar: 
            if score_croupier > 21:
                print('Croupier estourou! Você ganhou!')
                carteira += 2*valor_aposta
                printa_carteira()
                print('')
            elif score_croupier == score_jogador:
                print('Empatou!')
                carteira += valor_aposta
                printa_carteira()
                print('')
            elif score_jogador > score_croupier:
                print('Você ganhou!')
                carteira += 2*valor_aposta
                printa_carteira()
                print('')
            
            else: 
                print('Você perdeu!')
                printa_carteira()
                print('')
                            
            break 
               
        if primeira_mao and score_jogador == 21:
            print('Blackjack! Você ganhou!')
            carteira += 2.5*valor_aposta
            printa_carteira()
            print('')
            break

        primeira_mao = False

        if score_jogador == 21:
            print('Ganhou com 21!')
            carteira += 2*valor_aposta
            printa_carteira()
            print('')
            break

        if score_jogador > 21:
            print('Você estourou!')
            printa_carteira()
            print('')
            break

        print('O que você quer fazer? ')
        print('Digite:\n[1] para mais uma carta')
        print('[2] parar')
        
        print('')
        escolha = input('Escolha: ')
        print('')

        while escolha not in '1' and escolha not in '2':
            print('Valor inválido')
            escolha = input('Escolha: ')

        if escolha == '1':
            jogador.append(baralho.pop())
        elif escolha == '2':
            parar = True
            while calcula_mao(croupier) <= 17:
                croupier.append(baralho.pop())  
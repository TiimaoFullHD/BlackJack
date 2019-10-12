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


print('Com quantos baralhos você quer jogar?')
num_b = int(input('Digite entre 1 e 5: '))
while num_b > 5 or num_b < 1:
    num_b = int(input('Valor inválido!\nDigite um valor entre 1 e 5: '))
    
baralho = num_b*lista_b

carteira = 100

limpa()
valor_aposta = 0

#entrega cartas
parar = False
primeira_mao = True


print('BEM VINDO AO CASSINO DO DANIEL!')
print('')



while carteira > 0: 

    print('Você quer jogar?')
    print('')
    print('[1] para sim.')
    print('[2] para sair.')

    jogar_sair = int(input('Escolha: '))
    print('')

    while jogar_sair != 1 and jogar_sair!= 2:
        limpa()
        jogar_sair = int(input('Valor inválido!\n\nEscolha:\n[1] para jogar\n[2] para sair'))

    if jogar_sair == 1:
        print('')
    else: break
        
    limpa()
  
    parar = False
    primeira_mao = True
    
    printa_carteira()
    print('')
    valor_aposta = float(input('Digite o valor da aposta: '))

    while valor_aposta > carteira or valor_aposta < 0:
        print('Valor inválido')
        valor_aposta = float(input('Digite o valor da aposta: '))

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
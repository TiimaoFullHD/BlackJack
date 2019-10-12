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

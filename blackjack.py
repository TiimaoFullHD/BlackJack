import random, os

#funçoes 

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')


def printa_carteira():
    print(f'Carteira: {carteira}')
    
        
def calcula_mao(mao):
    soma = 0
#em andamento
from random import randint
print('=' * 50)
print('   Bem vindo ao jogo de pedra, papel e tesoura!')
print('=' * 50)
print('Você pode escolher as seguintes opções:')
print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura')
opcao = int(input('Com base no número, escolha a sua opção:')) - 1  # Adjust for zero-based index


itens = ['Pedra', 'Papel', 'Tesoura']


jogador = itens[opcao]
computador = itens[randint(1, 3)]
	
print(f'Jogador escolheu: {jogador}')
print(f'Computador escolheu: {computador}')

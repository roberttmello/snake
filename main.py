# 1 - Configurações iniciais
import pygame
import random

pygame.init()
pygame.display.set_caption('SNAKE')

LARGURA_TELA, ALTURA_TELA = 1366, 728
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
relogio = pygame.time.Clock()

# cores HEX
preto = '#000000'
branco = '#ffffff'
verde = '#00ff00'
amarelo = '#ffbb00'

# parâmetros do quadrado
tamanho_quadrado = 20
velocidade_cobra = 15

def gerar_comida():
    comida_pos_x = round(random.randrange(0, LARGURA_TELA - tamanho_quadrado) / tamanho_quadrado) * tamanho_quadrado
    comida_pos_y = round(random.randrange(0, ALTURA_TELA - tamanho_quadrado) / tamanho_quadrado) * tamanho_quadrado
    return comida_pos_x, comida_pos_y

# TODO Implementar função desenhar comida
def desenhar_comida():
    pass

# 2 - Criar um loop infinito
def rodar_jogo():
    fim_jogo = False
    cobra_posicao_x = LARGURA_TELA / 2
    cobra_posicao_y = ALTURA_TELA / 2
    velocidade_cobra_x = 0
    velocidade_cobra_y = 0
    tamanho_inicial_cobra = 1
    tamanho_cobra = []
    comida_pos_x, comida_pos_y = gerar_comida()

    while not fim_jogo:

        tela.fill(preto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True

        # Desenhar comida
        print(gerar_comida())

        relogio.tick(60)
        print(comida_pos_x, comida_pos_y)


rodar_jogo()
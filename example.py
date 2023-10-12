import pygame
import random

pygame.init()
LARGURA_TELA, ALTURA_TELA = 1280, 720
relogio = pygame.time.Clock()

# cores HEX
preto = '#222222'
branco = '#fafafa'
verde = '#00dd00'
amarelo = '#ffbb00'

tamanho_quadrado_pixels = 20
velocidade_jogo = 15

def gerar_comida():
    comida_pos_x = round(random.randrange(0, LARGURA_TELA - tamanho_quadrado_pixels) / tamanho_quadrado_pixels) * tamanho_quadrado_pixels
    comida_pos_y = round(random.randrange(0, ALTURA_TELA - tamanho_quadrado_pixels) / tamanho_quadrado_pixels) * tamanho_quadrado_pixels
    return comida_pos_x, comida_pos_y


def desenhar_comida(tela, tamanho, x_pos, y_pos):
    pygame.draw.rect(tela, amarelo, [x_pos, y_pos, tamanho, tamanho])


def desenhar_cobra(tela, tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branco, [pixel[0], pixel[1], tamanho, tamanho])


def desenhar_pontuacao(tela, pontuacao):
    fonte = pygame.font.Font('fonte/VT323-Regular.ttf', tamanho_quadrado_pixels * 2)
    texto = fonte.render(f'Pontos: {pontuacao}', False, verde)
    tela.blit(texto, (2,2))


def desenhar_fim_jogo(tela, pontuacao):
    fonte_1 = pygame.font.Font('fonte/VT323-Regular.ttf', tamanho_quadrado_pixels * 10)
    fonte_2 = pygame.font.Font('fonte/VT323-Regular.ttf', tamanho_quadrado_pixels * 5)

    texto_fim_jogo = fonte_1.render(f'FIM DE JOGO', False, verde)
    texto_pontuacao = fonte_2.render(f'Pontos: {pontuacao}', False, verde)

    tela.blit(texto_fim_jogo, (LARGURA_TELA/2, 2 * tamanho_quadrado_pixels))
    tela.blit(texto_pontuacao, (LARGURA_TELA / 2, 4 * tamanho_quadrado_pixels))

def selecionar_direcao(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado_pixels
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado_pixels
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado_pixels
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado_pixels
        velocidade_y = 0
    return velocidade_x, velocidade_y


def rodar_jogo():
    fim_jogo = False
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('SNAKE')

    cobra_posicao_x = LARGURA_TELA / 2
    cobra_posicao_y = ALTURA_TELA / 2
    velocidade_cobra_x = 0
    velocidade_cobra_y = 0
    tamanho_inicial_cobra = 1
    tamanho_pixels_cobra = []
    comida_pos_x, comida_pos_y = gerar_comida()
    deslocamento_cobra_x, deslocamento_cobra_y = 0, 0

    while True:
        if not fim_jogo:
            tela.fill(preto)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_jogo = True
                elif evento.type == pygame.KEYDOWN:
                    deslocamento_cobra_x, deslocamento_cobra_y = selecionar_direcao(evento.key)

            # Desenhar comida
            desenhar_comida(tela, tamanho_quadrado_pixels, comida_pos_x, comida_pos_y)

            # Atualizar a posicao da cobra
            cobra_posicao_x += deslocamento_cobra_x
            cobra_posicao_y += deslocamento_cobra_y

            # Verificando colisão com as paredes
            if cobra_posicao_x > LARGURA_TELA - tamanho_quadrado_pixels or cobra_posicao_x < 0:
                fim_jogo = True

            if cobra_posicao_y > ALTURA_TELA - tamanho_quadrado_pixels or cobra_posicao_y < 0:
                fim_jogo = True


        # Desenhar cobra
        tamanho_pixels_cobra.append((cobra_posicao_x, cobra_posicao_y))
        if len(tamanho_pixels_cobra) > tamanho_inicial_cobra:
            del tamanho_pixels_cobra[0]
        # Verificando colisao com o propio corpo
        for pedaco_cobra in tamanho_pixels_cobra[:-1]:
            if pedaco_cobra == (cobra_posicao_x, cobra_posicao_y):
                fim_jogo = True

            desenhar_cobra(tela, tamanho_quadrado_pixels, tamanho_pixels_cobra)
            desenhar_pontuacao(tela, tamanho_inicial_cobra - 1)

            # Criar uma nova comida
            if cobra_posicao_x == comida_pos_x and cobra_posicao_y == comida_pos_y:
                tamanho_pixels_cobra.append((comida_pos_x, comida_pos_y))
                desenhar_cobra(tela, tamanho_quadrado_pixels, tamanho_pixels_cobra)
                comida_pos_x, comida_pos_y = gerar_comida()
                tamanho_inicial_cobra += 1


            pygame.display.update()
            relogio.tick(velocidade_jogo)
        else:
            desenhar_fim_jogo(tela, tamanho_inicial_cobra - 1)
            pygame.display.update()
            relogio.tick(velocidade_jogo)

rodar_jogo()
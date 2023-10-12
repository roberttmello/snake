from sys import exit
import pygame
pygame.init()

# CORES DO JOGO
PRETO = '#222222'
BRANCO = '#FFEEDD'
AMARELO = '#FFBB00'
VERDE = '22FF22'


# DIMENSOES DA TELA
LARGURA_TELA, ALTURA_TELA = 1280, 720

# CRIANDO A TELA PRINCIPAL
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# CRIANDO RELÓGIO PARA CONTROLAR O FPS
relogio = pygame.time.Clock()

# VARIÁVEL QUE REPRESENTA o FPS do jogo
velocidade_jogo = 15

fim_de_jogo = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                fim_de_jogo = True



    tela.fill(PRETO)

    if not fim_de_jogo:
        fonte_1 = pygame.font.Font('fonte/VT323-Regular.ttf', int(20 * LARGURA_TELA / 100))
        fonte_2 = pygame.font.Font('fonte/VT323-Regular.ttf', int(5 * LARGURA_TELA / 100))

        nome_do_jogo = fonte_1.render('SNAKEpy', False, AMARELO)
        nome_do_jogo_ret = nome_do_jogo.get_rect(center=(LARGURA_TELA / 2, int(30 * ALTURA_TELA / 100)))

        mensagem = fonte_2.render("Pressione 'ESPAÇO' para começar", False, AMARELO)
        mensagem_ret = mensagem.get_rect(center=(LARGURA_TELA / 2, int(60 * ALTURA_TELA / 100)))

        tela.blit(nome_do_jogo, nome_do_jogo_ret)
        tela.blit(mensagem, mensagem_ret)


    else:
        fim_do_jogo = fonte_1.render('GAME OVER', False, AMARELO)
        fim_do_jogo_ret = fim_do_jogo.get_rect(center=(LARGURA_TELA / 2, int(30 * ALTURA_TELA / 100)))
        tela.blit(fim_do_jogo, fim_do_jogo_ret)

    pygame.display.flip()
    relogio.tick(velocidade_jogo)



pygame.quit()





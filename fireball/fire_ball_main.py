import pygame
import constantes
from classes import bola, nave_espacial, asteroide, tela_inicio
from classes.botoes import botao_retry, botao_play, botao_sair, botao_som
import os
import random


class Game:
    def __init__(self):
      # criando a tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode(
            (constantes.LARGURA_TELA, constantes.ALTURA_TELA))
        pygame.display.set_caption(constantes.NOME_JOGO)
        self.relogio = pygame.time.Clock()
        self.todos_os_botoes = pygame.sprite.Group()
        self.esta_rodando = True
        self.pontuacao = 0
        self.distancia_inicio = 20
        self.distancia_fim = 128
        self.velocidade_asteroide = 1
        self.tocar_sons = True
        self.carregar_arquivos()
        pygame.display.set_icon(self.imagem_icone)

    def carregar_arquivos(self):
      # carrega os arquivos da aplicação
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        diretorio_sons = os.path.join(os.getcwd(), 'sons')
        self.imagem_icone = os.path.join(
            diretorio_imagens, constantes.IMAGEM_ICONE)
        self.imagem_icone = pygame.image.load(self.imagem_icone).convert()

        self.imagem_game_fundo = os.path.join(
            diretorio_imagens, constantes.IMAGEM_GAME)
        self.imagem_game_fundo = pygame.image.load(
            self.imagem_game_fundo).convert()
        self.imagem_game_fundo = pygame.transform.scale(
            self.imagem_game_fundo, (constantes.LARGURA_TELA, constantes.ALTURA_TELA))

        self.imagem_game_over = os.path.join(
            diretorio_imagens, constantes.IMAGEM_GAME_OVER)
        self.imagem_game_over = pygame.image.load(
            self.imagem_game_over).convert()
        self.imagem_game_over = pygame.transform.scale(
            self.imagem_game_over, (constantes.LARGURA_TELA, constantes.ALTURA_TELA))

        self.som_bola_de_fogo = os.path.join(
            diretorio_sons, constantes.SOM_BOLA_DE_FOGO)
        self.som_bola_de_fogo = pygame.mixer.Sound(self.som_bola_de_fogo)
        self.som_bola_de_fogo.set_volume(constantes.VOLUME_TIRO_BOLA_DE_FOGO)

        self.som_explosao = os.path.join(
            diretorio_sons, constantes.SOM_EXPLOSAO)
        self.som_explosao = pygame.mixer.Sound(self.som_explosao)
        self.som_explosao.set_volume(constantes.VOLUME_EXPLOSAO)

        self.som_start = os.path.join(
            diretorio_sons, constantes.SOM_START)
        self.som_start = pygame.mixer.Sound(self.som_start)
        self.som_start.set_volume(constantes.VOLUME_START)

        self.som_game_over = os.path.join(
            diretorio_sons, constantes.SOM_GAME_OVER)
        self.som_game_over = pygame.mixer.Sound(self.som_game_over)
        self.som_game_over.set_volume(constantes.VOLUME_GAME_OVER)

    def novo_jogo(self):
        # instanciar as classes do jogo

        self.todas_as_sprites = pygame.sprite.Group()
        self.todos_os_asteroides = pygame.sprite.Group()
        self.todas_as_fireballs = pygame.sprite.Group()

        self.spacecraft = nave_espacial.NaveEspacial()
        self.todas_as_sprites.add(self.spacecraft)

        self.asteroid = asteroide.Asteroide(self.velocidade_asteroide)
        self.todos_os_asteroides.add(self.asteroid)

        self.rodar()

    def criar_fire_ball(self):
        # criando bola de fogo
        self.fire_ball = bola.Bola(self.spacecraft.posicoes_x_y())
        self.todas_as_fireballs.add(self.fire_ball)
        self.atualizar_sprites()
        if self.tocar_sons:
            self.som_bola_de_fogo.play()

    def criar_asteroides(self):
        # criar asteroides
        # este if diminui a distancia utilizada para geração de asteroides aleatoriamente
        # quanto menos o espaço, mais asteróides passarão a ser criados em menos tempo
        if constantes.PONTOS_PARA_AUMENTAR_QUANTIDADE_DE_ASTEROIDES.__contains__(self.pontuacao):
            self.distancia_inicio -= 2
            self.distancia_fim -= 5
            constantes.PONTOS_PARA_AUMENTAR_QUANTIDADE_DE_ASTEROIDES.remove(
                self.pontuacao)

        posicao_y_aleatoria = random.randrange(
            self.distancia_inicio, constantes.ALTURA_TELA-self.distancia_fim)

        if self.asteroid.posicoes_x_y()[1] > posicao_y_aleatoria or bool(self.todos_os_asteroides) == False:
            self.asteroid = asteroide.Asteroide(self.velocidade_asteroide)
            self.todos_os_asteroides.add(self.asteroid)

        self.atualizar_sprites()

    def rodar(self):
        # loop do jogo
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constantes.FPS)
            self.eventos()
            self.desenhar_sprites()

            self.colisoes_bola_asteroide = pygame.sprite.groupcollide(
                self.todos_os_asteroides, self.todas_as_fireballs, False, True, pygame.sprite.collide_mask)
            self.colisoes_asteroide_nave = pygame.sprite.spritecollide(
                self.spacecraft, self.todos_os_asteroides, True, pygame.sprite.collide_mask)

            if self.colisoes_bola_asteroide:

                for asteroide_bateu_bola in self.colisoes_bola_asteroide:
                    if self.tocar_sons:
                        self.som_explosao.play()
                    asteroide_bateu_bola.colidiu_com_fireball()

                self.pontuacao += 1
                # a cada 30 pontos (FREQUENCIA_DE_PONTOS),a velocidade dos asteroides aumenta em uma unidade
                velocidade = self.pontuacao/constantes.FREQUENCIA_DE_PONTOS
                if int(velocidade) != 0:
                    self.velocidade_asteroide = velocidade

            elif self.colisoes_asteroide_nave:
                if self.tocar_sons:
                    self.som_explosao.play()
                self.spacecraft.explodir_nave()
            else:
                self.criar_asteroides()
                self.atualizar_sprites()

            if self.spacecraft.terminou:
                self.spacecraft.kill()
                self.jogando = False
                self.abrir_tela_game_over = True

    def eventos(self):
        # define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False
                self.abrir_tela_game_over = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.criar_fire_ball()
                    self.fire_ball.atirar_bola_de_fogo()

    def atualizar_sprites(self):
        # atualiza sprites
        self.todas_as_sprites.update()
        self.todos_os_asteroides.update()
        self.todas_as_fireballs.update()

    def desenhar_sprites(self):
        # desenhar sprites
        self.tela.fill(constantes.COR_PRETA)  # limpando a tela
        self.tela.blit(self.imagem_game_fundo, (0, 0))
        self.todas_as_sprites.draw(self.tela)  # desenhando as sprites na tela
        self.todos_os_asteroides.draw(self.tela)
        self.todas_as_fireballs.draw(self.tela)
        texto_pontuacao = self.mostrar_textos(
            self.pontuacao, 40, (255, 255, 255), 'comicsansms')
        self.tela.blit(texto_pontuacao, (constantes.LARGURA_TELA - 100, 10))

        pygame.display.flip()

    def mostrar_textos(self, msg, tamanho, cor, estilo):
        fonte = pygame.font.SysFont(estilo, tamanho, True, False)
        mensagem = f'{msg}'
        texto = fonte.render(mensagem, True, cor)
        return texto

    def mostrar_tela_start(self):
        self.abrir_tela_start = True
        self.abrir_tela_game_over = False
        self.chuva_de_bolas = pygame.sprite.Group()
        self.mostrar_tela_start_e_game_over()
        # aqui para a execução da musica start do jogo
        self.som_start.stop()

    def mostrar_tela_game_over(self):
        self.abrir_tela_start = False
        self.mostrar_tela_start_e_game_over()
        # aqui para a execução da musica game over do jogo
        self.som_game_over.stop()

    def mostrar_tela_start_e_game_over(self):
        mensagem = ""
        posicao_x = 0
        posicao_y = 0

        if self.abrir_tela_start:
            mensagem = self.mostrar_textos(
                "FIRE B   LL", 60, constantes.COR_BRANCA, 'arial')
            posicao_x = constantes.LARGURA_TELA/2 - 160
            posicao_y = 200

            self.botao = botao_play.Play()
            self.botao_som = botao_som.BotaoSom()
            self.todos_os_botoes.add(self.botao_som)

            # começando música start do jogo
            if self.tocar_sons:
                self.som_start.play()

        elif self.abrir_tela_game_over:

            self.tela.blit(self.imagem_game_over, (0, 0))
            mensagem = self.mostrar_textos(
                "GAME OVER", 60, constantes.COR_BRANCA, 'arial')
            posicao_x = constantes.LARGURA_TELA/2 - 180
            posicao_y = 70

            self.botao = botao_retry.Retry()
            # começando música game over do jogo
            if self.tocar_sons:
                self.som_game_over.play()

        if self.abrir_tela_start or self.abrir_tela_game_over:
            posicao_x_botao_sair = self.botao.rect.centerx - 200
            posicao_y_botao_sair = self.botao.rect.centery

            self.botao_sair = botao_sair.Sair(
                posicao_x_botao_sair, posicao_y_botao_sair)
            self.todos_os_botoes.add(self.botao)
            self.todos_os_botoes.add(self.botao_sair)
            self.todos_os_botoes.draw(self.tela)

            pygame.mouse.set_visible(True)

        while self.abrir_tela_game_over or self.abrir_tela_start:
            if self.abrir_tela_start:
                if bool(self.chuva_de_bolas) == False or self.bola_da_chuva.rect.y <= random.randrange(constantes.ALTURA_TELA - 400, constantes.ALTURA_TELA):
                    self.bola_da_chuva = tela_inicio.TelaInicio()
                    self.chuva_de_bolas.add(self.bola_da_chuva)
                self.tela.fill(constantes.COR_PRETA)
                self.tela.blit(self.imagem_icone,
                               (constantes.LARGURA_TELA/2 + 30, 196))
                self.chuva_de_bolas.draw(self.tela)
                self.chuva_de_bolas.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.abrir_tela_start = False
                    self.esta_rodando = False
                    self.abrir_tela_game_over = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.botao.rect.collidepoint(pygame.mouse.get_pos()) and self.abrir_tela_game_over:
                        self.todos_os_botoes.empty()
                        self.abrir_tela_game_over = False
                        self.abrir_tela_start = False
                        self.setar_valores_padrao()
                    elif self.botao.rect.collidepoint(pygame.mouse.get_pos()) and self.abrir_tela_start:
                        self.todos_os_botoes.empty()
                        self.chuva_de_bolas.remove(self.chuva_de_bolas)
                        self.abrir_tela_start = False
                        self.esta_rodando = True
                    elif self.botao_som.rect.collidepoint(pygame.mouse.get_pos()):
                        self.botao_som.ligar_desligar_som()
                        self.tocar_sons = not self.botao_som.desligar_som
                        self.ligar_desligar_som_start()
                    elif self.botao_sair.rect.collidepoint(pygame.mouse.get_pos()):
                        self.abrir_tela_start = False
                        self.esta_rodando = False
                        self.abrir_tela_game_over = False

            self.tela.blit(mensagem, (posicao_x, posicao_y))
            self.todos_os_botoes.draw(self.tela)
            pygame.display.flip()
            self.todos_os_botoes.update()

    def setar_valores_padrao(self):
        self.pontuacao = 0
        self.velocidade_asteroide = 1
        self.distancia_inicio = 20
        self.distancia_fim = 128
        self.tocar_sons = True

    def ligar_desligar_som_start(self):
        if self.tocar_sons == False:
            self.som_start.stop()
        else:
            self.som_start.play()


game_fire_ball = Game()
game_fire_ball.mostrar_tela_start()
while game_fire_ball.esta_rodando:
    game_fire_ball.novo_jogo()
    game_fire_ball.mostrar_tela_game_over()

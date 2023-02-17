import pygame
import os
import constantes
import random


class Asteroide(pygame.sprite.Sprite):
    def __init__(self, velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_asteroide = []
        self.imagens_explosao = []
        self.carregar_arquivos()
        self.tamanho_aleatorio = random.randrange(64, 128)

        for linha in range(8):
            for coluna in range(8):
                imagem = self.sprite_sheet_asteroide.subsurface(
                    (coluna*128, linha*128), (128, 128))
                imagem = pygame.transform.scale(
                    imagem, (self.tamanho_aleatorio, self.tamanho_aleatorio))
                self.imagens_asteroide.append(imagem)

        for i in range(6):
            imagem_explosao = self.sprite_sheet_explosao.subsurface(
                (i*32, 0), (32, 32))
            imagem_explosao = pygame.transform.scale(
                imagem_explosao, (self.tamanho_aleatorio, self.tamanho_aleatorio))
            self.imagens_explosao.append(imagem_explosao)

        self.index_lista_asteroide = 0
        self.index_lista_explosao = 0

        self.image = self.imagens_asteroide[self.index_lista_asteroide]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (random.randrange(
            0, constantes.LARGURA_TELA-32), 0)

        if velocidade > 8:
            velocidade = 8

        self.velocidade_asteroide = velocidade
        self.colidiu = False
        self.mudou_imagem = False
        self.x_explosao = 0
        self.y_explosao = 0

    def update(self):
        self.x_explosao = self.rect.x
        self.y_explosao = self.rect.y
        if self.colidiu:
            if self.mudou_imagem == False:
                self.image = self.imagens_explosao[self.index_lista_explosao]
                self.rect = self.image.get_rect()
                self.rect.center = (self.x_explosao + 48, self.y_explosao + 48)
                self.mudou_imagem = True
            else:
                if self.index_lista_explosao > 5:
                    self.colidiu = False
                    self.kill()
                self.index_lista_explosao += 0.25
                self.image = self.imagens_explosao[int(
                    self.index_lista_explosao)]

        else:
            # aqui aumenta ou diminui a velocidade dos asteróides
            self.rect.y += self.velocidade_asteroide
            if self.rect.y >= constantes.ALTURA_TELA:
                self.kill()
            if self.index_lista_asteroide > 63:
                self.index_lista_asteroide = 0
            self.index_lista_asteroide += 0.25
            self.image = self.imagens_asteroide[int(
                self.index_lista_asteroide)]

    def carregar_arquivos(self):
        # Carrega as imagens correspondentes a classe asteroide
        diretorio_imagens_asteroide = os.path.join(os.getcwd(), 'imagens')
        self.sprite_sheet_asteroide = pygame.image.load(os.path.join(
            diretorio_imagens_asteroide, constantes.IMAGEM_ASTEROIDE)).convert_alpha()
        diretorio_imagens_explosao = os.path.join(os.getcwd(), 'imagens')
        self.sprite_sheet_explosao = pygame.image.load(os.path.join(
            diretorio_imagens_explosao, constantes.IMAGEM_EXPLOSAO)).convert_alpha()

    def posicoes_x_y(self):
        return (self.rect.x, self.rect.y)

    def colidiu_com_fireball(self):
        self.colidiu = True

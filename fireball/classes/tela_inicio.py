import pygame
import os
import constantes
import random


class TelaInicio(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_bola = []
        self.carregar_arquivos()
        tamanho = random.randrange(16, 32)
        for i in range(8):
            imagem = self.sprite_sheet_bola.subsurface((i*32, 0), (32, 32))
            imagem = pygame.transform.scale(imagem, (tamanho, tamanho))
            self.imagens_bola.append(imagem)
        self.index_lista = 0
        self.image = self.imagens_bola[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (random.randrange(
            0, constantes.LARGURA_TELA), constantes.ALTURA_TELA)

    def update(self):
        self.rect.y += -1
        if self.rect.bottomleft[1] <= 0 or self.rect.collidepoint(pygame.mouse.get_pos()):
            self.kill()
        if self.index_lista > 7:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_bola[int(self.index_lista)]

    def carregar_arquivos(self):
        # Carrega as imagens correspondentes a classe Bola
        diretorio_imagens_bola = os.path.join(os.getcwd(), 'imagens')
        self.sprite_sheet_bola = pygame.image.load(os.path.join(
            diretorio_imagens_bola, constantes.IMAGEM_BOLA)).convert_alpha()

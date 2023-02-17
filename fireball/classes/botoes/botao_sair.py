import pygame
import os
import constantes


class Sair(pygame.sprite.Sprite):
    def __init__(self, posicao_x, posicao_y):
        pygame.sprite.Sprite.__init__(self)
        self.carregar_arquivos()
        self.image = self.imagem_sair
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (posicao_x, posicao_y)

    def update(self):
        pass

    def carregar_arquivos(self):
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        self.imagem_sair = os.path.join(
            diretorio_imagens, constantes.IMAGEM_SAIR)
        self.imagem_sair = pygame.image.load(self.imagem_sair).convert()

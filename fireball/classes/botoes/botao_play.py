import pygame
import os
import constantes


class Play(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.carregar_arquivos()
        self.image = self.imagem_play
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (constantes.LARGURA_TELA/2 + 100,
                            constantes.ALTURA_TELA/2)
        # self.condicao = True

    def update(self):
        pass
        """ if self.condicao and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.condicao = False
        else:
            self.condicao = True """

    def carregar_arquivos(self):
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        self.imagem_play = os.path.join(
            diretorio_imagens, constantes.IMAGEM_PLAY)
        self.imagem_play = pygame.image.load(self.imagem_play).convert()

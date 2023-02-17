import pygame
import os
import constantes


class Retry(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.carregar_arquivos()
        self.image = self.imagem_retry
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (constantes.LARGURA_TELA/2 + 110,
                            constantes.ALTURA_TELA * 0.9)

    def update(self):
        pass
        """ if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.cursors.broken_x)
        else:
            pygame.mouse.set_cursor(pygame.cursors.arrow)
 """

    def carregar_arquivos(self):
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        self.imagem_retry = os.path.join(
            diretorio_imagens, constantes.IMAGEM_RETRY)
        self.imagem_retry = pygame.image.load(self.imagem_retry).convert()

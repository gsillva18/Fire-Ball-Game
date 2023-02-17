import pygame
import constantes
import os


class Bola(pygame.sprite.Sprite):
    def __init__(self, posicoes_x_y):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_bola = []
        self.carregar_arquivos()
        for i in range(8):
            imagem = self.sprite_sheet_bola.subsurface((i*32, 0), (32, 32))
            imagem = pygame.transform.scale(imagem, (32*0.5, 32*0.5))
            self.imagens_bola.append(imagem)
        self.index_lista = 0
        self.image = self.imagens_bola[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (posicoes_x_y[0] + 32, posicoes_x_y[1])
        self.atirar = False

    def update(self):
        if self.atirar:
            self.rect.y += -10
            if self.rect.bottomleft[1] <= 0:
                self.atirar = False
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

    def atirar_bola_de_fogo(self):
        self.atirar = True

    def posicoes_x_y(self):
        return (self.rect.x, self.rect.y)

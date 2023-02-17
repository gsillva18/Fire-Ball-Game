import pygame
import os
import constantes


class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_nave_espacial = []
        self.imagens_explosao = []
        self.carregar_arquivos()
        for i in range(5):
            imagem = self.sprite_sheet_nave_espacial.subsurface(
                (i*64, 0), (64, 64))
            self.imagens_nave_espacial.append(imagem)

        for i in range(6):
            imagem_explosao = self.sprite_sheet_explosao.subsurface(
                (i*32, 0), (32, 32))
            imagem_explosao = pygame.transform.scale(
                imagem_explosao, (100, 100))
            self.imagens_explosao.append(imagem_explosao)

        self.index_lista_explosao = 0
        self.index_lista_imagens_nave_espacial = 0
        self.image = self.imagens_nave_espacial[self.index_lista_imagens_nave_espacial]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        pygame.mouse.set_visible(False)
        self.rect.center = (constantes.LARGURA_TELA/2 - 32,
                            constantes.ALTURA_TELA - 40)
        self.colidiu = False
        self.mudou_imagem = False
        self.terminou = False
        self.x_explosao = 0
        self.y_explosao = 0

    def update(self):
        pygame.mouse.set_visible(False)
        if pygame.mouse.get_focused():
            self.rect.x = pygame.mouse.get_pos()[0] - 32
        if self.colidiu:
            if self.mudou_imagem == False:
                x_explosao = self.rect.x
                y_explosao = self.rect.y
                self.image = self.imagens_explosao[self.index_lista_explosao]
                self.rect = self.image.get_rect()
                self.rect.center = (x_explosao, y_explosao)
                self.mudou_imagem = True

            if self.index_lista_explosao > 5:
                self.colidiu = False
                self.terminou = True
            self.index_lista_explosao += 0.25
            self.image = self.imagens_explosao[int(self.index_lista_explosao)]

        else:
            if self.index_lista_imagens_nave_espacial > 4:
                self.index_lista_imagens_nave_espacial = 0
            self.index_lista_imagens_nave_espacial += 0.25
            self.image = self.imagens_nave_espacial[int(
                self.index_lista_imagens_nave_espacial)]

    def carregar_arquivos(self):
        # Carrega as imagens correspondentes a classe NaveEspacial
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
        self.sprite_sheet_nave_espacial = pygame.image.load(os.path.join(
            diretorio_imagens, constantes.IMAGEM_NAVE_ESPACIAL)).convert_alpha()
        self.sprite_sheet_explosao = pygame.image.load(os.path.join(
            diretorio_imagens, constantes.IMAGEM_EXPLOSAO)).convert_alpha()

    def posicoes_x_y(self):
        return (self.rect.x, self.rect.y)

    def explodir_nave(self):
        self.colidiu = True

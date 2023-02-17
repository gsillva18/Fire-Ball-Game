import pygame
import os
import constantes


class BotaoSom(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.carregar_arquivos()
        self.image = self.imagem_som_ligado
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (constantes.LARGURA_TELA - 50, 50)
        self.desligar_som = False
        self.mudar_imagem = False

    def update(self):
        if self.mudar_imagem:
            posicao_x_y_center = self.rect.center

            if self.desligar_som:
                self.image = self.imagem_som_desligado
            else:
                self.image = self.imagem_som_ligado

            self.rect = self.image.get_rect()
            # analisar para saber se realmente precisa dessa linha a baixo
            self.rect.center = posicao_x_y_center
            self.mudar_imagem = False

    def carregar_arquivos(self):
        diretorio_imagens = os.path.join(os.getcwd(), 'imagens')

        self.imagem_som_ligado = os.path.join(
            diretorio_imagens, constantes.IMAGEM_SOM_LIGADO)
        self.imagem_som_ligado = pygame.image.load(
            self.imagem_som_ligado).convert()
        self.imagem_som_ligado = pygame.transform.scale(
            self.imagem_som_ligado, (32, 32))

        self.imagem_som_desligado = os.path.join(
            diretorio_imagens, constantes.IMAGEM_SOM_DESLIGADO)
        self.imagem_som_desligado = pygame.image.load(
            self.imagem_som_desligado).convert()
        self.imagem_som_desligado = pygame.transform.scale(
            self.imagem_som_desligado, (32, 32))

    def ligar_desligar_som(self):
        self.mudar_imagem = True
        if self.desligar_som:
            self.desligar_som = False
        else:
            self.desligar_som = True

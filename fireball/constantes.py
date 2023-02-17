from tkinter import *
from tkinter.ttk import *
root = Tk()

# dimensões da tela
ALTURA_TELA = root.winfo_screenheight()
LARGURA_TELA = root.winfo_screenwidth()

# informações do jogo
NOME_JOGO = 'Fire Ball'

# Taxa de frames (FPS)
FPS = 30

# cores
COR_PRETA = (0, 0, 0)
COR_VERMELHA = (255, 0, 0)
COR_BRANCA = (255, 255, 255)

# imagens
IMAGEM_ICONE = 'bola-de-fogo-icone.png'
IMAGEM_NAVE_ESPACIAL = 'nave-espacial.png'
IMAGEM_BOLA = 'bola-de-fogo.png'
IMAGEM_ASTEROIDE = 'asteroide.png'
IMAGEM_EXPLOSAO = 'explosao.png'
IMAGEM_GAME = 'imagem-fundo.png'
IMAGEM_GAME_OVER = 'game-over-fundo.jpg'
IMAGEM_RETRY = 'retry.png'
IMAGEM_PLAY = 'play.png'
IMAGEM_SAIR = 'sair.png'
IMAGEM_SOM_LIGADO = 'som-ligado.png'
IMAGEM_SOM_DESLIGADO = 'som-desligado.png'

# sons
SOM_BOLA_DE_FOGO = "som-bola-de-fogo.wav"
SOM_EXPLOSAO = 'explosao.wav'
SOM_START = 'start.wav'
SOM_GAME_OVER = 'som-game-over.wav'

# volumes
VOLUME_TIRO_BOLA_DE_FOGO = 0.1
VOLUME_EXPLOSAO = 0.5
VOLUME_START = 1
VOLUME_GAME_OVER = 1

# quantidade de  variação pontos que quando alcançado aumenta a velocidade,
# ou seja, de x em x incremente um ponto a velocidade
FREQUENCIA_DE_PONTOS = 30

# valores de pontos que conduzirão alterações em ifs
PONTOS_PARA_AUMENTAR_QUANTIDADE_DE_ASTEROIDES = [
    20, 40, 60, 80, 100, 110, 120, 130, 140]

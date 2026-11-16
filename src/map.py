import pygame as pg
_ = False
# 0 será para as tarefas.

mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, 1, _, _, _, 1 , _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, 1 , _, _, _, _, _, _, _, 1],
    [1, _, _, 1, 1, _, 1, 1 , _, _, 1, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _ , _, _, 1, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _ , _, _, 1, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _ , _, _, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _ , _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class Map:
    """
    Essa classe recebe game.
    funções:
    get_map() recebe o mapa do jogo e o converte para o dicionário de pontos no mapa (world_map = {}), tal que J = [x] e I = [y]
    draw() desenha o mapa, aonde o mapa é 1 ele desenha paredes, aonde é _ ele não desenha.
    """
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgrey', (pos[0] * 100, pos[1] * 100, 100, 100), 2) 
        for pos in self.world_map]
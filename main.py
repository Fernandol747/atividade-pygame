from src.jogo import executar_jogo
import pygame # Base de todo esse projeto
import math # Seno, cosseno e Pi, pra podermos fazer o ray tracing.

pygame.init()
tela = pygame.display.set_mode((600, 400))
relogio = pygame.time.Clock()
mapa = [
        "##################",
        "#........#.......#",
        "#........#.......#",
        "#........##......#",
        "#................#",
        "#####......#.....#",
        "#..........#.....#",
        "#####......#.....#",
        "#..........#######",
        "#................#",
        "##################"
        ]



if __name__ == "__main__":
    # Ponto de entrada da aplicação.
    executar_jogo()
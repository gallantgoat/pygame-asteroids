import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    # we're making an infinite loop here for the game loop
    while True:
        # this is here so we can quit the game :)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000)
        player.draw(screen)
        pygame.display.flip()
        # We're calling tick here at the end of each iteration of the game loop
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()


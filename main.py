import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    # we're making an infinite loop here for the game loop
    while True:
        # this is here so we can quit the game :)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for object in updatable:
            object.update(dt)

        for object in asteroids:
            if object.collision_check(player) == True:
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if object.collision_check(bullet) == True:
                    object.kill()
                    bullet.kill()

        screen.fill(000)

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        # We're calling tick here at *the end* of each iteration of the game loop to limit the framerate
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()


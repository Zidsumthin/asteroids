# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    timer = pygame.time.Clock()
    dt = 0

    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shots.containers = (shots, updateable, drawable)

    my_character = Player(player_x, player_y)
    enemy_asteroids = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        updateable.update(dt)
        for i in asteroids:
            if i.collision_check(my_character) == True:
                print("Game over!")
                sys.exit()
        screen.fill((0,0,0))
        for i in drawable:
            i.draw(screen)
        
        pygame.display.flip()
        dt = timer.tick(60) / 1000
        

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
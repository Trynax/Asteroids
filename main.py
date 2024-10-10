import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid


def main():
   
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    Asteroid.containers = (asteroids_group, updatable, drawable)


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    player=Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    updatable.add(player)
    drawable.add(player)
    asteroid_field=AsteroidField()
    updatable.add(asteroid_field)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        screen.fill((0,0,0))


        for obj in updatable:
            obj.update(dt)
        
        for obj in drawable:
            obj.draw(screen)

        for asteriod in asteroids_group:
            if player.check_collision(asteriod):
                print("Game Over")
                pygame.quit()
                return
        pygame.display.flip()
        dt=fps.tick(60)/1000


if __name__ == "__main__":
    main()
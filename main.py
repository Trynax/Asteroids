import pygame
from constants import *
from player import Player



def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    player=Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    updatable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        screen.fill((0,0,0))


        for obj in updatable:
            obj.update(dt)
        
        for obj in drawable:
            obj.draw(screen)

            
        pygame.display.flip()
        dt=fps.tick(60)/1000


if __name__ == "__main__":
    main()
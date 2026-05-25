import pygame
from player import Player

pygame.init()

WIDTH = 1000
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Dino Shooter")

clock = pygame.time.Clock()

player = Player()

running = True

while running:

    clock.tick(60)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    player.move(keys)

    player.draw(screen)

    pygame.display.flip()

pygame.quit()

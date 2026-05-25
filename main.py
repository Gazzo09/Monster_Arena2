import pygame
import random
from player import Player
from enemy import Enemy

pygame.init()

WIDTH = 1000
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

player = Player()

enemies = []
spawn_timer = 0
spawn_rate = 120

font = pygame.font.SysFont(None, 40)

running = True

while running:

    clock.tick(60)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    player.move(keys)
    player.apply_gravity()
    player.draw(screen)

    spawn_timer += 1

    if spawn_timer >= spawn_rate:
        enemies.append(Enemy())
        spawn_timer = 0

    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)

    pygame.display.flip()

pygame.quit()

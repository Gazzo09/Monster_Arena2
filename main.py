import pygame
import random
from player import Player
from enemy import Enemy

pygame.init()

WIDTH = 1000
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Shooter")

clock = pygame.time.Clock()

player = Player()

# --- LISTA NEMICI (NUOVO) ---
enemies = []

# --- SPAWN TIMER (NUOVO) ---
spawn_timer = 0
spawn_rate = 120  # più basso = più nemici

font = pygame.font.SysFont(None, 40)

running = True

while running:

    clock.tick(60)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    # ---------------- PLAYER ----------------

    player.move(keys)
    player.apply_gravity()
    player.draw(screen)

    # ---------------- SPAWN ENEMIES ----------------

    spawn_timer += 1

    if spawn_timer >= spawn_rate:

        enemies.append(Enemy())  # crea nemico
        spawn_timer = 0

    # ---------------- ENEMIES UPDATE ----------------

    for enemy in enemies:

        enemy.move()
        enemy.draw(screen)

    # ---------------- UI ----------------

    lives_text = font.render(
        f"Vite: {player.lives}",
        True,
        (255, 255, 255)
    )

    screen.blit(lives_text, (20, 20))

    pygame.display.flip()

pygame.quit()

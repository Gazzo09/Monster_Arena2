import pygame
import random

from player import Player
from enemy import Enemy
from bullet import Bullet

pygame.init()

WIDTH = 1000
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Shooter")

clock = pygame.time.Clock()

player = Player()

enemies = []
bullets = []

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

        # 🔫 SPARO (COMMIT 10)
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_f:

                bullets.append(
                    Bullet(
                        player.x + player.width,
                        player.y + player.height // 2
                    )
                )

    # ---------------- BACKGROUND ----------------
    screen.fill((30, 30, 30))

    # ---------------- PLAYER ----------------
    player.move(keys)
    player.apply_gravity()
    player.draw(screen)

    # ---------------- SPAWN ENEMIES ----------------
    spawn_timer += 1

    if spawn_timer >= spawn_rate:
        enemies.append(Enemy())
        spawn_timer = 0

    # ---------------- UPDATE ENEMIES ----------------
    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)

    # ---------------- BULLETS UPDATE ----------------
    for bullet in bullets[:]:

        bullet.move()
        bullet.draw(screen)

        # elimina proiettile fuori schermo
        if bullet.x > WIDTH:
            bullets.remove(bullet)

    # ---------------- UI ----------------
    text = font.render(
        f"Vite: {player.lives}",
        True,
        (255, 255, 255)
    )

    screen.blit(text, (20, 20))

    pygame.display.flip()

pygame.quit()

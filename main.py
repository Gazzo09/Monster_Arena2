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

# 🟡 NUOVO: sistema kill
kills = 0

font = pygame.font.SysFont(None, 40)

running = True

while running:

    clock.tick(60)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # 🔫 SPARO
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

    # ---------------- ENEMIES UPDATE ----------------
    for enemy in enemies[:]:

        enemy.move()
        enemy.draw(screen)

        # ❌ se esce dallo schermo → perdi vita
        if enemy.x < -100:
            enemies.remove(enemy)
            player.lives -= 1

    # ---------------- BULLETS UPDATE + COLLISIONI ----------------
    for bullet in bullets[:]:

        bullet.move()
        bullet.draw(screen)

        # elimina fuori schermo
        if bullet.x > WIDTH:
            bullets.remove(bullet)
            continue

        # 🔥 COLLISIONE BULLET - ENEMY
        for enemy in enemies[:]:

            if bullet.rect().colliderect(enemy.rect()):

                enemies.remove(enemy)
                bullets.remove(bullet)

                kills += 1  # 🟡 AUMENTA KILL

                break

    # ---------------- UI ----------------
    text = font.render(
        f"Vite: {player.lives}  Kills: {kills}",
        True,
        (255, 255, 255)
    )

    screen.blit(text, (20, 20))

    pygame.display.flip()

pygame.quit()

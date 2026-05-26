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

kills = 0
level = 0

font = pygame.font.SysFont(None, 40)

running = True

while running:

    clock.tick(60)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:

                bullets.append(
                    Bullet(player.x + player.width, player.y + 20)
                )

    # ---------------- BACKGROUND ----------------
    screen.fill((30, 30, 30))

    # ---------------- PLAYER ----------------
    player.move(keys)
    player.apply_gravity()
    player.draw(screen)

    # ---------------- SPAWN ----------------
    spawn_timer += 1

    if spawn_timer >= spawn_rate:

        enemies.append(Enemy(level))  # 🟧 level passa ai nemici
        spawn_timer = 0

    # ---------------- ENEMIES ----------------
    for enemy in enemies[:]:

        enemy.move()
        enemy.draw(screen)

        # perdita vita se esce
        if enemy.x < -100:
            enemies.remove(enemy)
            player.lives -= 1

    # ---------------- BULLETS + COLLISIONI ----------------
    for bullet in bullets[:]:

        bullet.move()
        bullet.draw(screen)

        if bullet.x > WIDTH:
            bullets.remove(bullet)
            continue

        for enemy in enemies[:]:

            if bullet.rect().colliderect(enemy.rect()):

                enemy.hp -= player.damage  # 🟧 danno player

                bullets.remove(bullet)

                if enemy.hp <= 0:

                    enemies.remove(enemy)

                    kills += 1

                    # 🟧 LEVEL SYSTEM
                    if kills % 20 == 0:

                        level += 1
                        spawn_rate = max(25, spawn_rate - 10)

                        upgrade = random.choice([
                            "extra_life",
                            "more_damage",
                            "fast_shoot"
                        ])

                        player.apply_upgrade(upgrade)

                break

    # ---------------- UI ----------------
    ui = font.render(
        f"Vite: {player.lives}  Kills: {kills}  Level: {level}",
        True,
        (255, 255, 255)
    )

    screen.blit(ui, (20, 20))

    pygame.display.flip()

pygame.quit()

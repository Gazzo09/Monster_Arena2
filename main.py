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
big_font = pygame.font.SysFont(None, 80)

running = True

while running:

    clock.tick(60)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                # Controlla se il giocatore ha il super colpo caricato
                if player.super_shot_active:
                    new_bullet = Bullet(player.x + player.width, player.y + 20)
                    new_bullet.damage = 1000  # Modifica il danno del singolo proiettile
                    bullets.append(new_bullet)
                    player.super_shot_active = False  # Consuma il super colpo
                else:
                    bullets.append(
                        Bullet(player.x + player.width, player.y + 20)
                    )

    # ---------------- BACKGROUND ----------------
    screen.fill((30, 30, 30))

    # ---------------- GAME OVER CHECK ----------------
    if player.lives <= 0:

        game_over = big_font.render(
            "GAME OVER",
            True,
            (255, 0, 0)
        )

        screen.blit(game_over, (300, 200))

        stats = font.render(
            f"Kills: {kills}  Level: {level}",
            True,
            (255, 255, 255)
        )

        screen.blit(stats, (350, 300))

        pygame.display.flip()
        continue

    # ---------------- PLAYER ----------------
    player.move(keys)
    player.apply_gravity()
    player.draw(screen)

    # ---------------- SPAWN ----------------
    spawn_timer += 1

    if spawn_timer >= spawn_rate:

        enemies.append(Enemy(level))
        spawn_timer = 0

    # ---------------- ENEMIES ----------------
    for enemy in enemies[:]:

        enemy.move()
        enemy.draw(screen)

        if enemy.x < -100:
            enemies.remove(enemy)
            player.lives -= 1

    # ---------------- BULLETS ----------------
    for bullet in bullets[:]:

        bullet.move()
        bullet.draw(screen)

        if bullet.x > WIDTH:
            bullets.remove(bullet)
            continue

        for enemy in enemies[:]:

            if bullet.rect().colliderect(enemy.rect()):

                # Usa il danno specifico del proiettile se impostato, altrimenti quello del player
                damage_to_deal = getattr(bullet, 'damage', player.damage)
                enemy.hp -= damage_to_deal
                bullets.remove(bullet)

                if enemy.hp <= 0:

                    enemies.remove(enemy)
                    kills += 1

                    if kills % 20 == 0:

                        level += 1
                        spawn_rate = max(25, spawn_rate - 10)

                        # Allinea la scelta agli upgrade definiti nel file player
                        upgrade = random.choice([
                            "extra_life",
                            "more_speed",
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

    # Mostra lo stato degli upgrade (il set convertito in lista) e se il colpo speciale è pronto
    status_text = f"Upgrades: {list(player.upgrades)}"
    if player.super_shot_active:
        status_text += " [SUPER SHOT READY!]"

    upgrade_ui = font.render(
        status_text,
        True,
        (255, 255, 0)
    )

    screen.blit(upgrade_ui, (20, 60))

    pygame.display.flip()

pygame.quit()

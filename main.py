import pygame
import random

from player import Player
from enemy import Enemy
from bullet import Bullet

pygame.init()

WIDTH = 1000
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Zombie_Arena2")

clock = pygame.time.Clock()

player = Player()

enemies = []
bullets = []

spawn_timer = 0
spawn_rate = 120

kills = 0
level = 0

# Variabili per la gestione visiva del raggio rosso (special_shot)
special_shot_timer = 0
draw_special_shot = False

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

                enemy.hp -= player.damage
                enemy.hp -= 50
                bullets.remove(bullet)

                if enemy.hp <= 0:

                    enemies.remove(enemy)
                    kills += 1

                    if kills % 20 == 0:

                        level += 1
                        spawn_rate = max(25, spawn_rate - 10)

                        # Lista aggiornata dei potenziamenti utilizzabili
                        upgrade = random.choice([
                            "extra_life",
                            "more_damage",
                            "fast_shoot",
                            "more_speed"
                        ])

                        # CONTROLLO POTENZIAMENTO DOPPIO
                        if upgrade in player.upgrades:
                            
                            # Attiva l'effetto grafico dello special_shot
                            draw_special_shot = True
                            special_shot_timer = 100  # Durata del raggio in frame
                            
                            # Elimina tutti i nemici e aggiunge i punti alle uccisioni
                            for _ in enemies:
                                kills += 1
                            enemies.clear()
                            
                        else:
                            # Se non lo ha ancora, lo assegna normalmente
                            player.apply_upgrade(upgrade)

                break

    # ---------------- EFFECT: SPECIAL SHOT (RAGGIO ROSSO) ----------------
    if draw_special_shot:
        # Disegna un raggio distruttivo rosso che attraversa tutto lo schermo orizzontalmente
        laser_rect = pygame.Rect(0, 150, WIDTH, 200)
        pygame.draw.rect(screen, (255, 0, 0), laser_rect)
        
        special_shot_timer -= 1
        if special_shot_timer <= 0:
            draw_special_shot = False

    # ---------------- UI ----------------
    ui = font.render(
        f"Vite: {player.lives}  Kills: {kills}  Level: {level}",
        True,
        (255, 255, 255)
    )

    screen.blit(ui, (20, 20))

    upgrade_ui = font.render(
        f"Upgrades: {list(player.upgrades)}",
        True,
        (255, 255, 0)
    )

    screen.blit(upgrade_ui, (20, 60))

    pygame.display.flip()

pygame.quit()

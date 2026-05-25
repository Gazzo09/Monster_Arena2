import pygame
from player import Player

pygame.init()

WIDTH = 1000
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Dino Shooter")

clock = pygame.time.Clock()

player = Player()

# FONT (NUOVO)
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

    # ❤️ UI VITE (NUOVO)
    lives_text = font.render(
        f"Vite: {player.lives}",
        True,
        (255, 255, 255)
    )

    screen.blit(lives_text, (20, 20))

    pygame.display.flip()

pygame.quit()

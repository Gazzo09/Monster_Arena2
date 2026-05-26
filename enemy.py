import pygame
import random

class Enemy:

    def __init__(self, level):

        self.type = random.choice(["ground", "fly", "boss"])
        self.x = 1000
        self.speed = 4

        if self.type == "ground":
            self.y = 350
            self.width = 40
            self.height = 40
            self.hp = 200

        elif self.type == "fly":
            self.y = 250
            self.width = 40
            self.height = 40
            self.hp = 100

        else:
            self.y = 300
            self.width = 80
            self.height = 80
            self.hp = 400
            self.speed = 2  # boss lento

        # Genera la grafica in pixel art senza file esterni
        self.image = self.generate_pixel_art()

    def generate_pixel_art(self):
        # 1. Definiamo i colori (RGB)
        _ = (0, 0, 0, 0)          # Trasparente
        V = (34, 139, 34)         # Verde pelle zombie
        B = (70, 130, 180)        # Blu vestito
        P = (47, 79, 79)          # Grigio pantaloni
        R = (255, 0, 0)           # Rosso (occhi o dettagli)
        N = (0, 0, 0)             # Nero pupilla
        G = (140, 140, 140)       # Grigio (per le ali del tipo "fly")

        # 2. Definiamo i pattern 8x8 per tipo di nemico
        if self.type == "ground":
            grid = [
                [_, _, V, V, V, V, _, _],
                [_, V, R, V, V, R, V, _],
                [_, V, V, V, V, V, V, _],
                [_, _, B, B, B, B, _, _],
                [_, B, B, B, B, B, B, _],
                [_, _, P, P, P, P, _, _],
                [_, _, P, _, _, P, _, _],
                [_, V, V, _, _, V, V, _]
            ]
        elif self.type == "fly":
            grid = [
                [G, _, _, V, V, _, _, G],
                [G, G, V, R, R, V, G, G],
                [_, G, V, V, V, V, G, _],
                [_, _, B, B, B, B, _, _],
                [_, _, B, B, B, B, _, _],
                [_, _, P, P, P, P, _, _],
                [_, _, _, V, V, _, _, _],
                [_, _, _, _, _, _, _, _]
            ]
        else: # Boss (Zombie gigante arrabbiato)
            grid = [
                [_, V, V, V, V, V, V, _],
                [V, V, V, V, V, V, V, V],
                [V, N, R, V, V, R, N, V],
                [V, V, V, R, R, V, V, V],
                [_, B, B, B, B, B, B, _],
                [B, B, B, B, B, B, B, B],
                [_, P, P, P, P, P, P, _],
                [_, P, P, _, _, P, P, _]
            ]

        # 3. Creiamo una superficie quadrata temporanea (8x8 pixel)
        surf_8x8 = pygame.Surface((8, 8), pygame.SRCALPHA)
        
        # Disegniamo i pixel sulla superficie 8x8
        for y, row in enumerate(grid):
            for x, color in enumerate(row):
                surf_8x8.set_at((x, y), color)

        # 4. Scaliamo la superficie 8x8 alle dimensioni reali del nemico (width, height)
        final_surf = pygame.transform.scale(surf_8x8, (self.width, self.height))
        return final_surf

    def move(self):
        self.x -= self.speed

    def draw(self, screen):
        # Disegna lo zombie generato a schermo
        screen.blit(self.image, (self.x, self.y))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

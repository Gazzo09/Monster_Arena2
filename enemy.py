import pygame
import random

class Enemy:

    def __init__(self, level):

        self.type = random.choice(["ground", "fly", "boss"])
        self.x = 1000
        self.speed = 4

        # --- DIMENSIONI INGRANDITE ---
        if self.type == "ground":
            self.y = 330        # Abbassato leggermente per compensare l'altezza
            self.width = 60     # Ingrandito (da 40 a 60)
            self.height = 60    # Ingrandito (da 40 a 60)
            self.y = 350        
            self.width = 60     # Dimensione grande (60x60)
            self.height = 60    
            self.hp = 200

        elif self.type == "fly":
            self.y = 230        # Alzato per farlo volare meglio
            self.width = 60     # Ingrandito (da 40 a 60)
            self.height = 60    # Ingrandito (da 40 a 60)
            self.y = 230        # Posizione alta nel cielo
            self.width = 60     # Dimensione grande (60x60)
            self.height = 60    
            self.hp = 100

        else: # Boss
            self.y = 260        # Posizionato per la stazza del Boss
            self.width = 120    # Ingrandito (da 80 a 120)
            self.height = 120   # Ingrandito (da 80 a 120)
            self.y = 290        # Regolato per la stazza del Boss zombie
            self.width = 120    # Dimensione gigante (120x120)
            self.height = 120   
            self.hp = 400
            self.speed = 2  # boss lento

        # Genera la grafica degli UFO in pixel art
        # Genera la grafica mista (Zombie + UFO)
        self.image = self.generate_pixel_art()

    def generate_pixel_art(self):
        # Palette Colori UFO / Alieni
        # Palette Colori (Zombie + UFO)
        _ = (0, 0, 0, 0)            # Trasparente
        V = (34, 139, 34)           # Verde pelle zombie
        B = (70, 130, 180)          # Blu vestito zombie
        P = (47, 79, 79)            # Grigio pantaloni zombie
        R = (255, 0, 0)             # Rosso (Occhi zombie / Luci UFO)
        N = (0, 0, 0)               # Nero pupille
        G = (128, 128, 128)         # Grigio metallo UFO
        C = (0, 255, 255)           # Ciano (Vetro cabina / Raggio)
        R = (255, 0, 0)             # Rosso (Luci di segnalazione)
        V = (50, 205, 50)           # Verde Lime (Corpo Alieno)
        N = (0, 0, 0)               # Nero (Occhi alieno)
        O = (255, 165, 0)           # Arancione (Propulsori / Dettagli)
        C = (0, 255, 255)           # Ciano (Cupola vetro UFO)

        # Griglie 8x8 a tema UFO ed Alieni
        if self.type == "ground": # Piccolo Alieno in capsula terrestre
        # Griglie 8x8 differenziate per tipo di nemico
        if self.type == "ground": # ZOMBIE DI TERRA (60x60)
            grid = [
                [_, _, _, V, V, _, _, _],
                [_, _, N, V, V, N, _, _],
                [_, _, _, V, V, _, _, _],
                [_, _, C, C, C, C, _, _],
                [_, G, G, G, G, G, G, _],
                [G, G, O, G, G, O, G, G],
                [_, _, G, _, _, G, _, _],
                [_, O, _, _, _, _, O, _]
                [_, _, V, V, V, V, _, _],
                [_, V, R, V, V, R, V, _],
                [_, V, V, V, V, V, V, _],
                [_, _, B, B, B, B, _, _],
                [_, B, B, B, B, B, B, _],
                [_, _, P, P, P, P, _, _],
                [_, _, P, _, _, P, _, _],
                [_, V, V, _, _, V, V, _]
            ]
        elif self.type == "fly": # UFO Classico Volante
        elif self.type == "fly": # UFO VOLANTE (60x60)
            grid = [
                [_, _, _, C, C, _, _, _],
                [_, _, C, C, C, C, _, _],
                [_, G, G, G, G, G, G, _],
                [G, R, G, R, G, R, G, R],
                [G, G, G, G, G, G, G, G],
                [_, _, C, C, C, C, _, _],
                [_, _, C, _, _, C, _, _],
                [_, _, C, _, _, C, _, _]
            ]
        else: # Boss: Nave Madre UFO Gigante
        else: # BOSS: ZOMBIE GIGANTE ARRABBIATO (120x120)
            grid = [
                [_, _, _, _, G, G, _, _, _, _],
                [_, _, _, G, C, C, G, _, _, _],
                [_, _, G, G, C, C, G, G, _, _],
                [_, G, G, G, G, G, G, G, G, _],
                [G, R, G, R, G, R, G, R, G, R],
                [G, G, G, G, G, G, G, G, G, G],
                [_, G, O, O, G, G, O, O, G, _],
                [_, _, G, G, G, G, G, G, _, _]
                [_, _, V, V, V, V, V, V, _, _],
                [_, V, V, V, V, V, V, V, V, _],
                [_, V, N, R, V, V, R, N, V, _],
                [_, V, V, V, R, R, V, V, V, _],
                [_, _, B, B, B, B, B, B, _, _],
                [_, B, B, B, B, B, B, B, B, _],
                [_, _, P, P, P, P, P, P, _, _],
                [_, _, P, P, _, _, P, P, _, _],
                [_, _, P, _, _, _, _, P, _, _],
                [_, V, V, _, _, _, _, V, V, _]
            ]

        # Determina la dimensione della griglia sorgente (il boss usa 10x8 per essere più largo)
        # Rileva dinamicamente la forma della matrice (il boss usa una griglia 10x10)
        grid_width = len(grid[0])
        grid_height = len(grid)

        # Creiamo la superficie pixel art nativa
        surf_native = pygame.Surface((grid_width, grid_height), pygame.SRCALPHA)

        for y, row in enumerate(grid):
            for x, color in enumerate(row):
                surf_native.set_at((x, y), color)

        # Scaliamo la superficie alle nuove dimensioni ingrandite
        # Scaliamo la superficie alle dimensioni di gioco impostate
        final_surf = pygame.transform.scale(surf_native, (self.width, self.height))
        return final_surf

    def move(self):
        self.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

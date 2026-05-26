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
            # Carica l'immagine dello zombie a terra e la ridimensiona (40x40)
            self.image = pygame.image.load("zombie_ground.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

        elif self.type == "fly":
            self.y = 250
            self.width = 40
            self.height = 40
            self.hp = 100
            # Carica lo zombie volante o pipistrello (40x40)
            self.image = pygame.image.load("zombie_fly.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

        else:
            self.y = 300
            self.width = 80
            self.height = 80
            self.hp = 400
            self.speed = 2  # boss lento
            # Carica il boss zombie gigante (80x80)
            self.image = pygame.image.load("zombie_boss.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def move(self):
        self.x -= self.speed

    def draw(self, screen):
        # Sostituito pygame.draw.rect con screen.blit per disegnare l'immagine
        screen.blit(self.image, (self.x, self.y))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

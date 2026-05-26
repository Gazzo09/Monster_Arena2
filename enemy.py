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

    def move(self):
        self.x -= self.speed

    def draw(self, screen):

        color = (255, 0, 0)

        if self.type == "fly":
            color = (0, 0, 255)

        if self.type == "boss":
            color = (120, 0, 120)

        pygame.draw.rect(
            screen,
            color,
            (self.x, self.y, self.width, self.height)
        )

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

import pygame
import random

class Enemy:

    def __init__(self):

        self.type = random.choice(["ground", "fly"])

        self.x = 1000

        self.width = 40
        self.height = 40

        self.speed = 4

        if self.type == "ground":
            self.y = 350

        else:
            self.y = 250  # volanti più in alto

    def move(self):

        self.x -= self.speed

    def draw(self, screen):

        color = (255, 0, 0)

        if self.type == "fly":
            color = (0, 0, 255)

        pygame.draw.rect(
            screen,
            color,
            (self.x, self.y, self.width, self.height)
        )

    def rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

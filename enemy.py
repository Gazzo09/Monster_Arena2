import pygame

class Enemy:

    def __init__(self):

        self.x = 1000
        self.y = 350

        self.width = 40
        self.height = 40

        self.speed = 4

    def move(self):

        self.x -= self.speed

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (self.x, self.y, self.width, self.height)
        )

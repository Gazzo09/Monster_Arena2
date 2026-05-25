import pygame

class Bullet:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.width = 10
        self.height = 5

        self.speed = 10

    def move(self):
        self.x += self.speed

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            (255, 255, 0),
            (self.x, self.y, self.width, self.height)
        )

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

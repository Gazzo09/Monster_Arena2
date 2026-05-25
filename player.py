import pygame

class Player:

    def __init__(self):

        self.x = 100
        self.y = 350

        self.width = 50
        self.height = 50

        self.speed = 5

    def move(self, keys):

        if keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_d]:
            self.x += self.speed

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            (0,255,0),
            (self.x, self.y, self.width, self.height)
        )

import pygame

class Player:

    def __init__(self):

        self.x = 100
        self.y = 350

        self.width = 50
        self.height = 50

        self.speed = 5

        # salto
        self.vel_y = 0
        self.gravity = 0.8
        self.jump_power = -15
        self.on_ground = True

        # vite
        self.lives = 3

        # 🟡 NUOVO: set potenziamenti
        self.upgrades = set()

        # danno e sparo
        self.damage = 1
        self.fire_rate = 500

    def move(self, keys):

        if keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_d]:
            self.x += self.speed

        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

    def apply_gravity(self):

        self.vel_y += self.gravity
        self.y += self.vel_y

        if self.y >= 350:
            self.y = 350
            self.vel_y = 0
            self.on_ground = True

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (self.x, self.y, self.width, self.height)
        )

    # 🟡 NUOVO: sistema upgrade
    def apply_upgrade(self, upgrade):

        self.upgrades.add(upgrade)

        if upgrade == "extra_life":
            self.lives += 1

        elif upgrade == "more_damage":
            self.damage += 1

        elif upgrade == "fast_shoot":
            self.fire_rate = max(100, self.fire_rate - 100)

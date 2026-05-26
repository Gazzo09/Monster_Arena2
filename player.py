import pygame


class Player:

    def __init__(self):

        # posizione
        self.x = 100
        self.y = 350

        # dimensioni
        self.width = 60
        self.height = 80

        # movimento
        self.speed = 5

        # salto
        self.vel_y = 0
        self.gravity = 0.8
        self.jump_power = -15
        self.on_ground = True

        # stats
        self.max_lives = 5
        self.lives = 3

        # arma
        self.damage = 1
        self.fire_rate = 500

        # upgrade
        self.upgrades = set()

        # direzione player
        self.facing_right = True

        # colori
        self.body_color = (30, 120, 30)
        self.head_color = (50, 180, 50)
        self.gun_color = (40, 40, 40)

    def move(self, keys):

        if keys[pygame.K_a]:
            self.x -= self.speed
            self.facing_right = False

        if keys[pygame.K_d]:
            self.x += self.speed
            self.facing_right = True

        # salto
        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def jump(self):

        self.vel_y = self.jump_power
        self.on_ground = False

    def apply_gravity(self):

        self.vel_y += self.gravity
        self.y += self.vel_y

        # pavimento
        if self.y >= 350:
            self.y = 350
            self.vel_y = 0
            self.on_ground = True

    def draw(self, screen):

        #
        # ===== TESTA =====
        #
        pygame.draw.circle(
            screen,
            self.head_color,
            (self.x + 30, self.y + 20),
            20
        )

        #
        # ===== CORPO =====
        #
        pygame.draw.rect(
            screen,
            self.body_color,
            (self.x + 15, self.y + 40, 30, 40)
        )

        #
        # ===== BRACCIO =====
        #
        pygame.draw.line(
            screen,
            (20, 80, 20),
            (self.x + 30, self.y + 50),
            (self.x + 45, self.y + 60),
            6
        )

        #
        # ===== GAMBE =====
        #
        pygame.draw.line(
            screen,
            (0, 0, 255),
            (self.x + 20, self.y + 80),
            (self.x + 15, self.y + 105),
            6
        )

        pygame.draw.line(
            screen,
            (0, 0, 255),
            (self.x + 40, self.y + 80),
            (self.x + 45, self.y + 105),
            6
        )

        #
        # ===== FUCILE =====
        #
        if self.facing_right:

            # corpo arma
            pygame.draw.rect(
                screen,
                self.gun_color,
                (self.x + 40, self.y + 52, 35, 8)
            )

            # canna
            pygame.draw.rect(
                screen,
                (80, 80, 80),
                (self.x + 70, self.y + 54, 15, 4)
            )

        else:

            pygame.draw.rect(
                screen,
                self.gun_color,
                (self.x - 15, self.y + 52, 35, 8)
            )

            pygame.draw.rect(
                screen,
                (80, 80, 80),
                (self.x - 25, self.y + 54, 10, 4)
            )

    def apply_upgrade(self, upgrade):

        if upgrade in self.upgrades:
            Player.apply_special_shot()

        self.upgrades.add(upgrade)

        if upgrade == "extra_life":

            if self.lives < self.max_lives:
                self.lives += 1

        elif upgrade == "more_damage":

            self.damage += 25

        elif upgrade == "fast_shoot":

            self.fire_rate = max(100, self.fire_rate - 100)

        elif upgrade == "speed_boost":

            self.speed += 2

        elif upgrade == "super_jump":

            self.jump_power -= 3
    def apply_special_shot():
        enemy.hp-=1000

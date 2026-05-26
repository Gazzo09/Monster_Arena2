import random

UPGRADES = [
    "extra_life",
    "more_speed",
    "fast_shoot"
]

def random_upgrade():
    return random.choice(UPGRADES)


class Player:
    def __init__(self):
        # Parametri base del giocatore (adatta i valori alle tue esigenze)
        self.x = 100
        self.y = 300
        self.width = 50
        self.height = 50
        self.lives = 3
        self.damage = 1
        self.speed = 5
        
        # Gestione Upgrade tramite Set
        self.upgrades = set()
        self.super_shot_active = False

    def move(self, keys):
        # Logica di movimento base (esempio)
        import pygame
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    def apply_gravity(self):
        # Inserisci qui la tua logica della gravità se presente
        pass

    def draw(self, screen):
        # Logica temporanea di disegno del giocatore (quadrato verde)
        import pygame
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))

    def apply_upgrade(self, upgrade):
        # CONTROLLO TRAMITE SET: se l'upgrade è già presente nel set
        if upgrade in self.upgrades:
            self.super_shot_active = True
            print(f"Upgrade duplicato ({upgrade})! Super colpo caricato da 1000 danni!")
        else:
            # Se è nuovo, lo aggiunge al set e applica l'effetto
            self.upgrades.add(upgrade)
            
            if upgrade == "extra_life":
                self.lives += 1
            elif upgrade == "more_speed":
                self.speed += 2
            elif upgrade == "fast_shoot":
                # Logica per sparare più velocemente (es. riducendo un cooldown)
                pass
            print(f"Nuovo upgrade sbloccato: {upgrade}")

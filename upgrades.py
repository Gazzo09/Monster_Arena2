import random

UPGRADES = [
    "extra_life",
    "more_speed",
    "fast_shoot"
]

def random_upgrade():
    return random.choice(UPGRADES)

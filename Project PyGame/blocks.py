import pygame

PLATFORM_WIDTH = 42
PLATFORM_HEIGHT = 42
PLATFORM_COLOR = "#FF6262"
BLOCK_COLOR = "#fffe00"


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(pygame.Color(PLATFORM_COLOR))
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Block(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(pygame.Color(BLOCK_COLOR))


class EnemyPlatform(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.set_colorkey(pygame.Color(PLATFORM_COLOR))


class WinPlatform(EnemyPlatform):
    def __init__(self, x, y):
        EnemyPlatform.__init__(self, x, y)




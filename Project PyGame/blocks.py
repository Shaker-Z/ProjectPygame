import pygame

PLATFORM_WIDTH = 42
PLATFORM_HEIGHT = 42
FL_PLATFORM_WIDTH = 42
FL_PLATFORM_HEIGHT = 21
PLATFORM_COLOR = "#FF6262"
BLOCK_COLOR = "#fffe00"


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('data/objects/castleCenter.png').convert(),
                                            (PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Block(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.transform.scale(pygame.image.load('data/objects/boxCoin.png').convert(),
                                            (PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.set_colorkey((0, 0, 0))


class FlyingPlatform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('data/objects/bridge.png').convert(),
                                            (FL_PLATFORM_WIDTH, FL_PLATFORM_HEIGHT))
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.Rect(x, y, FL_PLATFORM_WIDTH, FL_PLATFORM_HEIGHT)
        self.tik = [0, False]

    def fall(self):
        self.tik[1] = True

    def update(self):
        if self.tik[1]:
            self.tik[0] += 1
        if self.tik[0] >= 20:
            self.rect.y += 3
        if self.tik[0] >= 200:
            self.kill()


class EnemyPlatform(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.set_colorkey((0,0,0))


class WinPlatform(EnemyPlatform):
    def __init__(self, x, y):
        EnemyPlatform.__init__(self, x, y)





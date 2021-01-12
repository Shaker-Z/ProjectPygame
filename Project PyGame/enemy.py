import pygame

MOVE_SPEED = 2
WIDTH = 32
HEIGHT = 27
HG_WIDTH = 27
HG_HEIGHT = 27
EN_COLOR = "#ff1111"
HG_COLOR = "#fffe33"
GRAVITY = 0.35


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = MOVE_SPEED
        self.startX = x
        self.startY = y
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(pygame.Color(EN_COLOR))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.yvel = 0
        self.onGround = False
        self.killable = True

    def update(self,  platforms, hero, enemys):
        if not self.onGround:
            self.yvel += GRAVITY
        self.onGround = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, enemys)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms, enemys)

    def collide(self, xvel, yvel, platforms, enemys):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.xvel *= -1

                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.xvel *= -1

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0


class Hedgehog(Enemy):
    def __init__(self, x, y):
        Enemy.__init__(self, x, y)
        self.image = pygame.Surface((HG_WIDTH, HG_HEIGHT))
        self.image.fill(pygame.Color(HG_COLOR))
        self.rect = pygame.Rect(x, y, HG_WIDTH, HG_HEIGHT)
        self.killable = False

    def hide(self):
        self.killable = True
        self.xvel = MOVE_SPEED + 3.5
        self.image = pygame.Surface((WIDTH+3, HEIGHT))
        self.image.fill(pygame.Color(HG_COLOR))
        self.rect = pygame.Rect(self.rect.x, self.rect.y, WIDTH+3, HEIGHT)

    def collide(self, xvel, yvel, platforms, enemys):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.xvel *= -1

                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.xvel *= -1

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0

        if self.killable:
            for e in enemys:
                if pygame.sprite.collide_rect(self, e):
                    if e != self:
                        e.kill()




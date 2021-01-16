import pygame

MOVE_SPEED = 2
WIDTH = 38
HEIGHT = 33
HG_WIDTH = 33
HG_HEIGHT = 33
TM_WIDTH = 41
TM_HEIGHT = 45
EN_COLOR = "#ff1111"
HG_COLOR = "#fffe33"
TM_COLOR = "#11fffe"
GRAVITY = 0.35


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = -MOVE_SPEED
        self.startX = x
        self.startY = y
        self.image = pygame.transform.scale(pygame.image.load('data/enemys/slime.png').convert(),
                                            (WIDTH, HEIGHT))
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.yvel = 0
        self.onGround = False
        self.killable = True

    def update(self, platforms, enemys):

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
        self.image = pygame.transform.scale(pygame.image.load('data/enemys/snail.png').convert(),
                                            (HG_WIDTH, HG_HEIGHT))
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.Rect(x, y, HG_WIDTH, HG_HEIGHT)
        self.killable = False

    def hide(self):
        self.killable = True
        self.xvel = MOVE_SPEED + 3
        self.image = pygame.transform.scale(pygame.image.load('data/enemys/snail_shell.png').convert(),
                                            (WIDTH, HEIGHT))
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.Rect(self.rect.x, self.rect.y, WIDTH, HEIGHT)

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


class Termite(pygame.sprite.Sprite):
    def __init__(self, x, y, platform):
        pygame.sprite.Sprite.__init__(self)
        self.startX = x
        self.startY = y
        self.image = pygame.transform.scale(pygame.image.load('data/enemys/barnacle.png').convert(),
                                            (TM_WIDTH, TM_HEIGHT))
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.Rect(x+2, y, TM_WIDTH, TM_HEIGHT)
        self.yvel = MOVE_SPEED - 1
        self.platfom = platform
        self.tik = 0
        self.killable = False

    def update(self, platforms, enemys):
        if self.rect.midbottom == self.platfom.rect.midtop:
            self.rect.bottom = self.platfom.rect.top
            self.tik = 0 if self.tik == 200 else self.tik
            self.tik += 1
        if self.rect.midbottom == self.platfom.rect.midbottom:
            self.rect.bottom = self.platfom.rect.bottom
            self.tik = 0 if self.tik == 200 else self.tik
            self.tik += 1
        if self.tik == 200:
            self.move()

    def move(self):
        if self.rect.midbottom == self.platfom.rect.midtop:
            self.yvel *= -1
        if self.rect.midbottom == self.platfom.rect.midbottom:
            self.yvel = abs(self.yvel)
        self.rect.y -= self.yvel






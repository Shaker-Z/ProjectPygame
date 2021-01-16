import pygame

MOVE_SPEED = 5
WIDTH = 38
HEIGHT = 38
JUMP_POWER = 11
GRAVITY = 0.35
COLOR = "#888888"


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.hp = 5
        self.xvel = 0
        self.start_pos = (x, y)
        # self.image = pygame.Surface((WIDTH, HEIGHT))
        # self.image.fill(pygame.Color(COLOR))
        self.original_image = pygame.transform.scale(pygame.image.load('data/enemys/alienYellow_badge1.png').convert(),
                                                     (WIDTH, HEIGHT))
        self.image = self.original_image
        self.angle = 0
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.yvel = 0
        self.onGround = False
        self.clock = pygame.time.Clock()

    def update(self, left, right, up, platforms, enemys):
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
        if left:
            self.xvel = -MOVE_SPEED
            self.angle += 4 % 360
            if 20 <= abs(self.angle) <= 70 or 110 <= abs(self.angle) <= 160 or \
                    200 <= abs(self.angle) <= 250 or 290 <= abs(self.angle) <= 340:
                self.image = pygame.transform.scale(pygame.transform.rotate(self.original_image, self.angle).convert(),
                                                    (WIDTH + 6, HEIGHT + 6))
            else:
                self.image = pygame.transform.scale(pygame.transform.rotate(self.original_image, self.angle).convert(),
                                                    (WIDTH, HEIGHT))

        if right:
            self.xvel = MOVE_SPEED
            self.angle -= 4 % 360
            if 20 <= abs(self.angle) <= 70 or 110 <= abs(self.angle) <= 160 or \
                    200 <= abs(self.angle) <= 250 or 290 <= abs(self.angle) <= 340:
                self.image = pygame.transform.scale(pygame.transform.rotate(self.original_image, self.angle).convert(),
                                                    (WIDTH + 6, HEIGHT + 6))
            else:
                self.image = pygame.transform.scale(pygame.transform.rotate(self.original_image, self.angle).convert(),
                                                    (WIDTH, HEIGHT))
        if not (left or right):
            self.xvel = 0
        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, enemys)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms, enemys)

        if self.on_enemy(enemys) and self.clock.get_time() > 100:
            self.hp -= 1
            print(self.hp)

    def collide(self, xvel, yvel, platforms, enemys):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):

                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                    if p.__class__.__name__ == 'FlyingPlatform':
                        p.fall()

                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0
                    if p.__class__.__name__ == 'Block':
                        p.kill()
                        del platforms[platforms.index(p)]
        for e in enemys:
            if pygame.sprite.collide_rect(self, e):
                if (self.rect.collidepoint(e.rect.midtop[0], e.rect.midtop[1]+5) or
                        self.rect.collidepoint(e.rect.topleft[0] + 5, e.rect.topleft[1]) or
                        self.rect.collidepoint(e.rect.topright[0] - 5, e.rect.topright[1])) and \
                        not self.onGround and self.on_enemy(enemys) and self.clock.get_time() > 100:
                    self.yvel = -JUMP_POWER * 0.6
                    if e.killable:
                        e.kill()
                    elif e.__class__.__name__ == 'Hedgehog':
                        e.hide()
                    elif e.__class__.__name__ == 'Termite':
                        self.hp -= 1
                        print(self.hp)

    def on_enemy(self, enemys):
        for e in enemys:
            if self.rect.collidepoint(e.rect.midleft) or self.rect.collidepoint(e.rect.midright):
                self.yvel = -JUMP_POWER * 0.5
                self.clock.tick()
                return True
        return False

    def is_win(self, win_platforms):
        for wp in win_platforms:
            if pygame.sprite.collide_rect(self, wp):
                return True
        return False


import pygame

MOVE_SPEED = 5
WIDTH = 35
HEIGHT = 35
JUMP_POWER = 11
GRAVITY = 0.35
COLOR = "#888888"


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.hp = 1
        self.score = 0
        self.xvel = 0
        self.start_pos = (x, y)
        self.original_image = pygame.transform.scale(pygame.image.load('data/enemys/kolobok.png').convert(),
                                                     (WIDTH, HEIGHT))
        self.image = self.original_image
        self.angle = 0
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.yvel = 0
        self.onGround = False
        self.clock = pygame.time.Clock()
        self.jump_sound = pygame.mixer.Sound('data/sounds/jump.mp3')
        self.jump_sound.set_volume(0.25)
        self.coin_get_sound = pygame.mixer.Sound('data/sounds/coin.mp3')
        self.coin_get_sound.set_volume(0.25)

    def update(self, left, right, up, platforms, enemys, coins):
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
                self.jump_sound.play()
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
        self.collide(0, self.yvel, platforms, enemys, coins)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms, enemys, coins)

        if self.on_enemy(enemys) and self.clock.get_time() > 100:
            self.hp -= 1
            print(self.hp)

    def collide(self, xvel, yvel, platforms, enemys, coins):
        for p in pygame.sprite.groupcollide(platforms, pygame.sprite.GroupSingle(self), False, False):
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
                    if p.__class__.__name__ == 'ItemBlock':
                        p.item.rect.y -= p.item.rect.h
                        p.item.active = True
        for e in pygame.sprite.groupcollide(enemys, pygame.sprite.GroupSingle(self), False, False):
            if pygame.sprite.collide_rect(self, e):
                if (self.rect.collidepoint(e.rect.midtop[0], e.rect.midtop[1]+5) or
                        self.rect.collidepoint(e.rect.topleft[0] + 5, e.rect.topleft[1]) or
                        self.rect.collidepoint(e.rect.topright[0] - 5, e.rect.topright[1])) and \
                        not self.onGround and self.on_enemy(enemys) and self.clock.get_time() > 100:
                    self.yvel = -JUMP_POWER * 0.6
                    if e.killable:
                        e.kill()
                        self.score += 10
                    elif e.__class__.__name__ == 'Hedgehog':
                        e.hide()
                    elif e.__class__.__name__ == 'Termite':
                        self.hp -= 1
                        print(self.hp)
                if e.__class__.__name__ == 'Cherry':
                    e.kill()
                    self.hp += 1
                    print(self.hp)

        for c in pygame.sprite.groupcollide(coins, pygame.sprite.GroupSingle(self), False, False):
            self.score += 5
            self.coin_get_sound.play()
            c.kill()

    def on_enemy(self, enemys):
        for e in enemys:
            if (self.rect.collidepoint(e.rect.midleft) or self.rect.collidepoint(e.rect.midright)) \
                    and e.__class__.__name__ != 'Cherry':
                self.yvel = -JUMP_POWER * 0.5
                self.clock.tick()
                return True
        return False

    def is_win(self, win_platforms):
        for wp in win_platforms:
            if pygame.sprite.collide_rect(self, wp):
                return True
        return False


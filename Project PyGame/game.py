from blocks import *
from player import *
from enemy import *
import pygame, subprocess

WIN_WIDTH = 1000
WIN_HEIGHT = 700
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIN_WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - WIN_HEIGHT // 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Super Kolobok Bros")
    timer = pygame.time.Clock()
    entities = pygame.sprite.Group()
    enemys = pygame.sprite.Group()
    updateble_platforms = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    fl_platforms = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    enemy_platforms = pygame.sprite.Group()
    win_platforms = []
    camera = Camera()
    with open('lvl.txt', mode='rt', encoding='utf8') as lvl:
        levelname = f'level{lvl.read()}.txt'
    if levelname == 'level2.txt':
        pos = 'under'
        bg = pygame.transform.scale(pygame.image.load('data/objects/bg_castle.png').convert(), (WIN_WIDTH, WIN_HEIGHT))
        pygame.mixer.music.load('data/sounds/underground-saundtrak.mp3')
    else:
        pos = 'up'
        bg = pygame.transform.scale(pygame.image.load('data/objects/bg_grasslands.png').convert(), (WIN_WIDTH, WIN_HEIGHT))
        pygame.mixer.music.load('data/sounds/saundtrek.mp3')
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(loops=100)
    with open(levelname, mode='rt', encoding='utf-8') as fl_level:
        level = fl_level.readlines()
    x = 0
    y = 0
    f = True
    for row in level[::-1]:
        for col in row:
            if col == '^':
                pf = Wall(x, y)
                updateble_platforms.add(pf)
                entities.add(pf)
                platforms.add(pf)
                enemy_platforms.add(pf)
                tm = Termite(x, y, pf)
                entities.add(tm)
                enemys.add(tm)
            if col == '-':
                if f:
                    pf = Platform(x, y, pos)
                    f = False
                else:
                    t = Platform(x, y, pos)
                    entities.add(t)
                    pf.rect = pf.rect.union(t.rect)
            elif pf not in entities:
                entities.add(pf)
                platforms.add(pf)
                enemy_platforms.add(pf)
                f = True

            if col == 'w':
                wl = Wall(x, y)
                entities.add(wl)
                platforms.add(wl)
                enemy_platforms.add(wl)

            if col == '#':
                bl = Block(x, y)
                cn = Coin(x, y)
                entities.add(cn)
                coins.add(cn)
                entities.add(bl)
                platforms.add(bl)
                enemy_platforms.add(bl)
            if col == '&':
                ch = Cherry(x, y)
                entities.add(ch)
                enemys.add(ch)
                ib = ItemBlock(x, y, ch)
                entities.add(ib)
                platforms.add(ib)
                enemy_platforms.add(ib)
            if col == 'C':
                cn = Coin(x, y)
                entities.add(cn)
                coins.add(cn)
            if col == '_':
                fp = FlyingPlatform(x, y)
                entities.add(fp)
                platforms.add(fp)
                fl_platforms.add(fp)
            if col == '%':
                ep = EnemyPlatform(x, y)
                entities.add(ep)
                enemy_platforms.add(ep)
            if col == '*':
                hero = Player(x, y)
                entities.add(hero)
            if col == '+':
                en = Enemy(x, y)
                entities.add(en)
                enemys.add(en)
            if col == '=':
                hg = Hedgehog(x, y)
                entities.add(hg)
                enemys.add(hg)
            if col == '!':
                wp = WinPlatform(x, y)
                entities.add(wp)
                win_platforms.append(wp)

            x += PLATFORM_WIDTH
        y -= PLATFORM_HEIGHT
        x = 0
    left = right = False
    up = False
    running = True
    font = pygame.font.Font(None, 50)
    while running:
        screen.blit(bg, (0, 0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True
            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False

            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False

            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False

        camera.update(hero)
        hero.update(left, right, up, platforms, enemys, coins)
        enemys.update(enemy_platforms, enemys)
        fl_platforms.update()

        for sprite in entities:
            camera.apply(sprite)
        entities.draw(screen)
        updateble_platforms.draw(screen)
        text = font.render(str(hero.score).rjust(5, '0'), True, (204, 50, 50))
        text_rect = text.get_rect(topleft=(15, 15))
        screen.blit(text, text_rect)
        x, y = 15, WIN_HEIGHT - 50
        for i in range(hero.hp):
            t = HP(x, y)
            screen.blit(t.image, t.rect)
            x += t.rect.w + 5
        pygame.display.update()
        timer.tick(60)
        if hero.hp == 0:
            running = False
        if hero.is_win(win_platforms):
            running = False


if __name__ == "__main__":
    main()
    pygame.quit()
    subprocess.call(['python', 'START.py'], shell=True)
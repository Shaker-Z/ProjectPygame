from blocks import *
from player import *
from enemy import *
import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 640
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
    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    timer = pygame.time.Clock()
    bg.fill(pygame.Color(BACKGROUND_COLOR))
    entities = pygame.sprite.Group()
    enemys = pygame.sprite.Group()
    platforms = []
    enemy_platforms = []
    win_platforms = []
    camera = Camera()
    with open('level.txt', mode='rt', encoding='utf-8') as fl_level:
        level = fl_level.readlines()
    x = 0
    y = 0
    for row in level[::-1]:
        for col in row:
            if col == '-':
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
                enemy_platforms.append(pf)
            if col == '#':
                bl = Block(x, y)
                entities.add(bl)
                platforms.append(bl)
            if col == '%':
                ep = EnemyPlatform(x, y)
                entities.add(ep)
                enemy_platforms.append(ep)
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
    while running:
        screen.blit(bg, (0, 0))
        timer.tick(60)
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
        hero.update(left, right, up, platforms, enemys)
        enemys.update(enemy_platforms, hero, enemys)

        for sprite in entities:
            camera.apply(sprite)
        entities.draw(screen)
        pygame.display.update()

        if hero.hp == 0:
            running = False
        if hero.is_win(win_platforms):
            running = False


if __name__ == "__main__":
    main()
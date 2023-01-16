#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Импортируем библиотеку pygame
import pygame
from pygame import *
from player import *
from blocks import *
from monsters import *

# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную

FILE_DIR = os.path.dirname(__file__)


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - WIN_WIDTH), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - WIN_HEIGHT), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return Rect(l, t, w, h)


def loadLevel(num):
    global playerX, playerY, monsters1  # объявляем глобальные переменные, это координаты героя
    levelFile = open(f'levels/{str(num)}.txt')
    line = " "
    commands = []
    while line[0] != "/":  # пока не нашли символ завершения файла
        line = levelFile.readline()  # считываем построчно
        if line[0] == "[":  # если нашли символ начала уровня
            while line[0] != "]":  # то, пока не нашли символ конца уровня
                line = levelFile.readline()  # считываем построчно уровень
                if line[0] != "]":  # и если нет символа конца уровня
                    endLine = line.find("|")  # то ищем символ конца строки
                    level.append(line[0: endLine])  # и добавляем в уровень строку от начала до символа "|"

        if line[0] != "":  # если строка не пустая
            commands = line.split()  # разбиваем ее на отдельные команды
            if len(commands) > 1:  # если количество команд > 1, то ищем эти команды
                if commands[0] == "player":  # если первая команда - player
                    playerX = int(commands[1])  # то записываем координаты героя
                    playerY = int(commands[2])
                if commands[0] == "portal":  # если первая команда portal, то создаем портал
                    tp = BlockTeleport(int(commands[1]), int(commands[2]), int(commands[3]), int(commands[4]))
                    entities.add(tp)
                    platforms.append(tp)
                    animatedEntities.add(tp)
                if commands[0] == "monster":  # если первая команда monster, то создаем монстра
                    mn = Monster(int(commands[1]), int(commands[2]), int(commands[3]), int(commands[4]),
                                 int(commands[5]), int(commands[6]))
                    entities.add(mn)
                    platforms.append(mn)
                    monsters1.add(mn)


def main(num):
    pygame.init()  # Инициация PyGame, обязательная строчка
    global hero, screen, level, monsters1, entities, animatedEntities, platforms
    level = []
    entities = pygame.sprite.Group()  # Все объекты
    animatedEntities = pygame.sprite.Group()  # все анимированные объекты, за исключением героя
    monsters1 = pygame.sprite.Group() # Все передвигающиеся объекты
    platforms = []  # то, во что мы будем врезаться или опираться

    loadLevel(num)

    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Super Mario Boy")  # Пишем в шапку
    bg = pygame.image.load('bg.gif')  # добавляем фоновое изображение

    pygame.mixer.music.load("saundtrack.mp3")
    pygame.mixer.music.play(-1)

    button = pygame.image.load('Design/pause\pause.png')
    button_rect = button.get_rect(topright=(800, 0))

    left = right = False  # по умолчанию - стоим
    up = False
    running = False

    label = pygame.font.Font('font.otf', 40)



    win_label = pygame.image.load('Design/result/victory.png')
    loose_label = pygame.image.load('Design/result/loose_img.png')

    continue_button = pygame.image.load('Design/pause/continue.png')
    continue_button_rect = continue_button.get_rect(topleft=(296, 255))

    go_back = pygame.image.load('Design/pause/go_back.png')
    go_back_rect = go_back.get_rect(topleft=(296, 322))

    go_back_button = label.render('Меню', False, (255, 255, 255))
    go_back_button_rect = go_back_button.get_rect(topleft=(330, 400))

    pause_im = pygame.image.load('Design/pause/pause_menu_bg.png')

    restart_label = pygame.image.load('Design/result/restart_button.png')
    restart_label_rect = restart_label.get_rect(topleft=(222, 520))

    hero = Player(playerX, playerY)  # создаем героя по (x,y) координатам
    entities.add(hero)

    timer = pygame.time.Clock()
    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "*":
                bd = BlockDie(x, y)
                entities.add(bd)
                platforms.append(bd)
            if col == "P":
                pr = Princess(x, y)
                entities.add(pr)
                platforms.append(pr)
                animatedEntities.add(pr)

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
    total_level_height = len(level) * PLATFORM_HEIGHT  # высоту

    camera = Camera(camera_configure, total_level_width, total_level_height)
    gameplay = True
    c = 0
    while True:  # Основной цикл программы
        if not hero.winner:
            timer.tick(60)
            if hero.not_die:
                if gameplay:
                    c = 0
                    pygame.mixer.music.unpause()
                    for e in pygame.event.get():  # Обрабатываем события
                        if e.type == QUIT:
                            raise SystemExit
                        if e.type == KEYDOWN and e.key == K_UP:
                            up = True
                        if e.type == KEYDOWN and e.key == K_LEFT:
                            left = True
                        if e.type == KEYDOWN and e.key == K_RIGHT:
                            right = True
                        if e.type == KEYDOWN and e.key == K_LSHIFT:
                            running = True

                        if e.type == KEYUP and e.key == K_UP:
                            up = False
                        if e.type == KEYUP and e.key == K_RIGHT:
                            right = False
                        if e.type == KEYUP and e.key == K_LEFT:
                            left = False
                        if e.type == KEYUP and e.key == K_LSHIFT:
                            running = False

                    screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

                    animatedEntities.update()  # показываеaм анимацию
                    monsters1.update(platforms)# передвигаем всех монстров
                    camera.update(hero)  # центризируем камеру относительно персонажа
                    hero.update(left, right, up, running, platforms)  # передвижение
                    for e in entities:
                        screen.blit(e.image, camera.apply(e))
                        # обновление и вывод всех изменений на экран
                    screen.blit(button, button_rect)
                    mouse = pygame.mouse.get_pos()
                    if button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                        gameplay = False


                else:
                    if c == 0:
                        screen.blit(bg, (0, 0))  # смотреть
                        animatedEntities.update()  # Показываеaм анимацию
                        monsters1.update(platforms)# передвигаем всех монстров
                        camera.update(hero)  # центризируем камеру относительно персонажа
                        hero.update(left, right, up, running, platforms)  # передвижение
                        for e in entities:
                            screen.blit(e.image, camera.apply(e))
                            # обновление и вывод всех изменений на экран
                    pygame.mixer.music.pause()
                    screen.blit(pause_im, (0, 0))
                    screen.blit(continue_button, continue_button_rect)
                    screen.blit(go_back, go_back_rect)
                    mouse = pygame.mouse.get_pos()
                    if continue_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                        gameplay = True
                    for e in pygame.event.get():  # Обрабатываем события
                        if e.type == QUIT:
                            raise SystemExit
                        if e.type == MOUSEBUTTONDOWN and go_back_rect.collidepoint(mouse):
                            return 1
                    c = 1
            else:
                pygame.mixer.music.pause()
                screen.blit(loose_label, (0, 0))
                screen.blit(restart_label, restart_label_rect)
                mouse = pygame.mouse.get_pos()
                if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    right = left = running = up = False
                    hero.not_die = True
                    hero.sound_die.stop()
                    pygame.mixer.music.set_pos(0.0)
                for e in pygame.event.get():  # Обрабатываем события
                    if e.type == QUIT:
                        raise SystemExit
        else:
            pygame.mixer.music.pause()
            screen.blit(win_label, (0, 0))
            for e in pygame.event.get():  # Обрабатываем события
                if e.type == QUIT:
                    raise SystemExit

        pygame.display.update()


level = []
entities = pygame.sprite.Group()  # Все объекты
animatedEntities = pygame.sprite.Group()  # все анимированные объекты, за исключением героя
monsters1 = pygame.sprite.Group()  # Все передвигающиеся объекты
platforms = []  # то, во что мы будем врезаться или опираться
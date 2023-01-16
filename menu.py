import sys
import pygame
from main_of_pygame_part import main

WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
pygame.init()  # Инициация PyGame, обязательная строчка


def menu(need_anim):
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)  # Создание окна
    pygame.display.set_caption("Super Mario Boy")  # Название
    bg = pygame.image.load('Design/menu/menu_bg.png')  # Фоновое изображение

    menu_im = pygame.image.load('Design/menu/logo.png')

    start_button = pygame.image.load('Design/menu/start_menu_button.png')  # Создание кнопок для меню
    start_button_rect = start_button.get_rect(topleft=(276, 251))
    instruction_button = pygame.image.load('Design/menu/instruction_button.png')
    instruction_button_rect = instruction_button.get_rect(topleft=(276, 319))
    exit_button = pygame.image.load('Design/menu/exit_button.png')
    exit_button_rect = exit_button.get_rect(topleft=(276, 387))

    instructions_img = pygame.image.load('Design/instructions/instructions.png')

    go_back_to_menu = pygame.image.load('Design/instructions/go_back.png')
    go_back_to_menu_rect = go_back_to_menu.get_rect(topleft=(38, 585))

    go_back_to_menu2 = pygame.image.load('Design/instructions/go_back.png')
    go_back_to_menu_rect2 = go_back_to_menu.get_rect(topleft=(53, 585))

    levels_bg = pygame.image.load('Design/levels_menu/level_menu.png')

    level_1 = pygame.image.load('Design/levels_menu/1_level.png')  # Создание кнопок для меню
    level_1_rect = level_1.get_rect(topleft=(276, 251))
    level_2 = pygame.image.load('Design/levels_menu/2_level.png')
    level_2_rect = level_2.get_rect(topleft=(276, 319))
    level_3 = pygame.image.load('Design/levels_menu/3_level.png')
    level_3_rect = level_3.get_rect(topleft=(276, 387))

    clock = pygame.time.Clock()

    chose_level = False  # Переменные для сосотояния окна
    instructions = False

    if need_anim:
        while True:
            menu_b_y = -176
            while menu_b_y != 62:
                clock.tick(1500)
                screen.fill('#cb2229')
                screen.blit(menu_im, (218, menu_b_y))
                menu_b_y += 0.5
                pygame.display.update()

            while menu_b_y != 10:
                clock.tick(200)
                screen.fill('#cb2229')
                screen.blit(menu_im, (218, menu_b_y))
                menu_b_y -= 1
                pygame.display.update()
            while menu_b_y != 62:
                clock.tick(200)
                screen.fill('#cb2229')
                screen.blit(menu_im, (218, menu_b_y))
                menu_b_y += 1
                pygame.display.update()

            while menu_b_y != 20:
                clock.tick(200)
                screen.fill('#cb2229')
                screen.blit(menu_im, (218, menu_b_y))
                menu_b_y -= 1
                pygame.display.update()
            while menu_b_y != 62:
                clock.tick(200)
                screen.fill('#cb2229')
                screen.blit(menu_im, (218, menu_b_y))
                menu_b_y += 1
                pygame.display.update()

            while menu_b_y != 30:
                clock.tick(200)
                screen.fill('#cb2229')
                screen.blit(menu_im, (218, menu_b_y))
                menu_b_y -= 1
                pygame.display.update()
            while menu_b_y != 62:
                clock.tick(200)
                screen.fill('#cb2229')
                screen.blit(menu_im, (218, menu_b_y))
                menu_b_y += 1
                pygame.display.update()

            while menu_b_y != 40:
                clock.tick(200)
                screen.fill('#cb2229')
                screen.blit(menu_im, (218, menu_b_y))
                menu_b_y -= 1
                pygame.display.update()
            while menu_b_y != 62:
                clock.tick(200)
                screen.fill('#cb2229')
                screen.blit(menu_im, (218, menu_b_y))
                menu_b_y += 1
                pygame.display.update()

            while menu_b_y != 50:
                clock.tick(200)
                screen.fill('#cb2229')
                screen.blit(menu_im, (218, menu_b_y))
                menu_b_y -= 1
                pygame.display.update()
            while menu_b_y != 62:
                clock.tick(200)
                screen.fill('#cb2229')
                screen.blit(menu_im, (218, menu_b_y))
                menu_b_y += 1
                pygame.display.update()

            start_b_x = -251
            while start_b_x != 276:
                clock.tick(1100)
                screen.fill('#cb2229')
                screen.blit(menu_im, (218, 62))
                screen.blit(start_button, (start_b_x, 251))
                start_b_x += 1
                pygame.display.update()

            inst_b_x = 891
            while inst_b_x != 276:
                clock.tick(1100)
                screen.fill('#cb2229')
                screen.blit(menu_im, (218, 62))
                screen.blit(start_button, ((276, 251)))
                screen.blit(instruction_button, (inst_b_x, 319))
                inst_b_x -= 1
                pygame.display.update()

            start_b_x = -251
            while start_b_x != 276:
                clock.tick(1100)
                screen.fill('#cb2229')
                screen.blit(menu_im, (218, 62))
                screen.blit(start_button, ((276, 251)))
                screen.blit(instruction_button, ((276, 319)))
                screen.blit(exit_button, (start_b_x, 387))
                start_b_x += 1
                pygame.display.update()
            break

    while not chose_level and not instructions:
        screen.blit(bg, (0, 0))
        screen.blit(menu_im, (218, 62))
        screen.blit(start_button, start_button_rect)
        screen.blit(instruction_button, instruction_button_rect)
        screen.blit(exit_button, exit_button_rect)
        mouse = pygame.mouse.get_pos()
        if start_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            chose_level = True
        if instruction_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            instructions = True
        if exit_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            raise SystemExit
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == pygame.constants.QUIT:
                raise SystemExit
        pygame.display.update()
    while chose_level:
        pygame.init()
        screen.blit(levels_bg, (0, 0))
        screen.blit(level_1, level_1_rect)
        screen.blit(level_2, level_2_rect)
        screen.blit(level_3, level_3_rect)
        screen.blit(go_back_to_menu2, go_back_to_menu_rect2)

        mouse = pygame.mouse.get_pos()

        if go_back_to_menu_rect2.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            chose_level = False
            menu(False)

        for e in pygame.event.get():  # Обрабатываем события
            if e.type == pygame.constants.QUIT:
                raise SystemExit
            if level_1_rect.collidepoint(mouse) and e.type == pygame.MOUSEBUTTONDOWN:
                if main(1) == 2:
                    if main(2) == 2:
                        main(3)

            if level_2_rect.collidepoint(mouse) and e.type == pygame.MOUSEBUTTONDOWN:
                if main(2) == 2:
                    main(3)
            if level_3_rect.collidepoint(mouse) and e.type == pygame.MOUSEBUTTONDOWN:
                main(3)

        pygame.display.update()
    while instructions:
        screen.blit(instructions_img, (0, 0))
        screen.blit(go_back_to_menu, go_back_to_menu_rect)
        mouse = pygame.mouse.get_pos()
        if go_back_to_menu_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            instructions = False
            menu(False)
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == pygame.constants.QUIT:
                raise SystemExit
        pygame.display.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    menu(True)

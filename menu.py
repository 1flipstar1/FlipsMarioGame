from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from main_of_pygame_part import main
import pygame

WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)


def menu():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Super Mario Boy")  # Пишем в шапку
    bg = pygame.image.load('Меню-1.png')  # добавляем фоновое изображение
    continue_button = pygame.image.load('blocks\dieBlock.png')
    continue_button_rect = continue_button.get_rect(topleft=(280, 250))
    chose_level = False
    while not chose_level:
        screen.blit(bg, (0, 0))
        screen.blit(continue_button, continue_button_rect)
        mouse = pygame.mouse.get_pos()
        if continue_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            chose_level = True
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == pygame.constants.QUIT:
                raise SystemExit
        pygame.display.update()
    while chose_level:
        screen.fill((125, 42, 238))
        #screen.blit(bg, (0, 0))
        #screen.blit(continue_button, continue_button_rect)
        mouse = pygame.mouse.get_pos()
        if continue_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            chose_level = True
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == pygame.constants.QUIT:
                raise SystemExit
        pygame.display.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    menu()

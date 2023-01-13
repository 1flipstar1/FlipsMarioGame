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
    while True:
        screen.blit(bg, (0, 0))
        pygame.display.update()
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == pygame.constants.QUIT:
                raise SystemExit



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    menu()




from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from main_of_pygame_part import main


class SMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('arbuz.ui', self)
        d = QPixmap('Портал-1.png')
        a = QPixmap('Меню-1.png')
        # self.lb.setPixmap(d)
        # self.lb2.setPixmap(a)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.close)
        self.pb3.clicked.connect(self.choce_lvl1)

    def choce_lvl1(self):
        lvl_win = LevelWindow()
        lvl_win.show()
        '''if __name__ == '__main__':
            app = QtWidgets.QApplication(sys.argv)
            
            sys.excepthook = except_hook
            sys.exit(app.exec_())'''

    def run(self):
        self.close()
        if __name__ == "__main__":

            main(2)



class LevelWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('levels_menu.ui', self)
        self.lvl1.clicked.connect(self.starts)
        self.lvl2.clicked.connect(self.starts)
        self.lvl3.clicked.connect(self.starts)

    def starts(self, num_of_lvl=5):
        print(1)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = SMainWindow()
    MainWindow.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())




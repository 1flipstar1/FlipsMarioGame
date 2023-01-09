from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from main_of_pygame_part import main

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('arbuz.ui', self)
        d = QPixmap('Портал-1.png')
        a = QPixmap('Меню-1.png')
        self.lb.setPixmap(d)
        self.lb2.setPixmap(a)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.close)



    """def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Минипланировщик"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))"""

    def run(self):
        self.close()
        if __name__ == "__main__":
            main(2)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())


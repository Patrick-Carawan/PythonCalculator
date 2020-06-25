import sys
from PyQt5.QtWidgets import QApplication, QLabel

class Calculator():
    def __init__(self):
        self.window()

    def window(self):
        app = QApplication([])
        label = QLabel('Hello World!')
        label.show()
        app.exec_()


if __name__ == '__main__':
    Calculator()

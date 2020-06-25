import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget


class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.makegui()

    def makegui(self):
        label = QLabel('One day this will be a calculator!')
        layout = QHBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        self.show()



def main():
    app = QApplication([])
    calc = Calculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


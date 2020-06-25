import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import *

class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.makegui()

    def makegui(self):

        # All our buttons are here
        zero = QPushButton("0")
        one = QPushButton("1")
        two = QPushButton("2")
        three = QPushButton("3")
        four = QPushButton("4")
        five = QPushButton("5")
        six = QPushButton("6")
        seven = QPushButton("7")
        eight = QPushButton("8")
        nine = QPushButton("9")
        plus = QPushButton("+")
        minus = QPushButton("-")
        times = QPushButton("*")
        divide = QPushButton("/")
        dot = QPushButton(".")
        equals = QPushButton("=")

        # The calculator has a four column layout
        first_col = QVBoxLayout()
        second_col = QVBoxLayout()
        third_col = QVBoxLayout()
        fourth_col = QVBoxLayout()

        # User's history will appear above the screen
        history = QLabel()

        # Creating a Regex validator to limit inputs to numbers and appropriate symbols
        regex = QRegExp("\\d*")
        num_validator = QRegExpValidator(regex)

        screen = QLineEdit()
        screen.setAlignment(Qt.AlignRight)
        screen.setValidator(num_validator)

        zero_and_divide_container = QHBoxLayout()
        button_container = QHBoxLayout()
        screen_and_button_container = QVBoxLayout()

        first_col.addWidget(seven)
        first_col.addWidget(four)
        first_col.addWidget(one)

        second_col.addWidget(eight)
        second_col.addWidget(five)
        second_col.addWidget(two)

        third_col.addWidget(nine)
        third_col.addWidget(six)
        third_col.addWidget(three)

        fourth_col.addWidget(plus)
        fourth_col.addWidget(minus)
        fourth_col.addWidget(times)

        button_container.addLayout(first_col)
        button_container.addLayout(second_col)
        button_container.addLayout(third_col)
        button_container.addLayout(fourth_col)

        zero_and_divide_container.addWidget(dot)
        zero_and_divide_container.addWidget(zero)
        zero_and_divide_container.addWidget(equals)
        zero_and_divide_container.addWidget(divide)

        screen_and_button_container.addWidget(history)
        screen_and_button_container.addWidget(screen)
        screen_and_button_container.addLayout(button_container)
        screen_and_button_container.addLayout(zero_and_divide_container)

        self.setLayout(screen_and_button_container)
        self.show()


def main():
    app = QApplication([])
    calc = Calculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


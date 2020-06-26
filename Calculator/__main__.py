import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QShortcut
from PyQt5.QtGui import QRegExpValidator, QKeySequence
from PyQt5.QtCore import *


class Calculator(QWidget):

    function = False
    operator = None

    def __init__(self):
        super().__init__()

        # User's history will appear above the screen
        self.screen = QLineEdit()
        self.history = QLabel()

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

        # Shortcuts for buttons

        zero_shortcut = QShortcut("0", zero)
        zero_shortcut.activated.connect(zero.animateClick)

        one_shortcut = QShortcut("1", one)
        one_shortcut.activated.connect(one.animateClick)

        two_shortcut = QShortcut("2", two)
        two_shortcut.activated.connect(two.animateClick)

        three_shortcut = QShortcut("3", three)
        three_shortcut.activated.connect(three.animateClick)

        four_shortcut = QShortcut("4", four)
        four_shortcut.activated.connect(four.animateClick)

        five_shortcut = QShortcut("5", five)
        five_shortcut.activated.connect(five.animateClick)

        six_shortcut = QShortcut("6", six)
        six_shortcut.activated.connect(six.animateClick)

        seven_shortcut = QShortcut("7", seven)
        seven_shortcut.activated.connect(seven.animateClick)

        eight_shortcut = QShortcut("8", eight)
        eight_shortcut.activated.connect(eight.animateClick)

        nine_shortcut = QShortcut("9", nine)
        nine_shortcut.activated.connect(nine.animateClick)



        # Creating a Regex validator to limit inputs to numbers and appropriate symbols
        regex = QRegExp("\\d*(?:\\.\\d+)?")
        num_validator = QRegExpValidator(regex)

        # Screen is a one line text box using the above Regex validator
        self.screen.setAlignment(Qt.AlignRight)
        self.screen.setValidator(num_validator)

        # The calculator has a four column layout
        first_col = QVBoxLayout()
        second_col = QVBoxLayout()
        third_col = QVBoxLayout()
        fourth_col = QVBoxLayout()

        # Creating Layout
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

        screen_and_button_container.addWidget(self.history)
        screen_and_button_container.addWidget(self.screen)
        screen_and_button_container.addLayout(button_container)
        screen_and_button_container.addLayout(zero_and_divide_container)

        # Assigning button methods

        zero.clicked.connect(self.zero)
        one.clicked.connect(self.one)
        two.clicked.connect(self.two)
        three.clicked.connect(self.three)
        four.clicked.connect(self.four)
        five.clicked.connect(self.five)
        six.clicked.connect(self.six)
        seven.clicked.connect(self.seven)
        eight.clicked.connect(self.eight)
        nine.clicked.connect(self.nine)

        plus.clicked.connect(self.add)
        minus.clicked.connect(self.subtract)
        times.clicked.connect(self.multiply)
        divide.clicked.connect(self.divide)
        equals.clicked.connect(self.equals)

        self.setLayout(screen_and_button_container)
        self.show()

    # Number Functions
    def zero(self):
        self.screen.setText(self.screen.text()+'0')

    def one(self):
        self.screen.setText(self.screen.text()+'1')

    def two(self):
        self.screen.setText(self.screen.text()+'2')

    def three(self):
        self.screen.setText(self.screen.text() + '3')

    def four(self):
        self.screen.setText(self.screen.text() + '4')

    def five(self):
        self.screen.setText(self.screen.text()+'5')

    def six(self):
        self.screen.setText(self.screen.text()+'6')

    def seven(self):
        self.screen.setText(self.screen.text()+'7')

    def eight(self):
        self.screen.setText(self.screen.text()+'8')

    def nine(self):
        self.screen.setText(self.screen.text()+'9')

    # Calculator functions
    def add(self):

        if self.function:
            self.history.setText(str(int(self.history.text())+int(self.screen.text())))
            self.screen.setText('')
        elif self.screen.text():
            self.history.setText(self.screen.text())
            self.screen.setText('')
        else:
            x=None

        self.function = True
        self.operator = "plus"

    def subtract(self):
        print("Placeholder")

    def multiply(self):
        print("Placeholder")

    def divide(self):
        print("Placeholder")

    def equals(self):
        if self.operator == "plus":
            self.history.setText(str(int(self.history.text())+int(self.screen.text())))
            self.screen.setText('')
        self.operator = None
        self.function = False


def main():
    app = QApplication([])
    calc = Calculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


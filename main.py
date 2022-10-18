import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from design import Ui_MainWindow
from operator import add, sub, mul, truediv, mod, pow
import math

result = None
znak = None
flag = False


class Calculator(QMainWindow):

    def __init__(self):

        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # digits
        self.ui.btn_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.btn_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.btn_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.btn_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.btn_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.btn_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.btn_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.btn_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.btn_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.btn_9.clicked.connect(lambda: self.add_digit('9'))

        # actions
        self.ui.btn_clear.clicked.connect(lambda: self.clear_all())
        self.ui.btn_CE.clicked.connect(lambda: self.clear_le())
        self.ui.btn_backspace.clicked.connect(lambda: self.backspace())
        self.ui.btn_point.clicked.connect(lambda: self.add_point())
        self.ui.btn_cos.clicked.connect(lambda: self.btn_cosinus())
        self.ui.btn_sin.clicked.connect(lambda: self.btn_sinus())
        self.ui.btn_plus.clicked.connect(lambda: self.calculate('+'))
        self.ui.btn_div.clicked.connect(lambda: self.calculate('/'))
        self.ui.btn_equals.clicked.connect(lambda: self.calculate('='))
        self.ui.btn_multip.clicked.connect(lambda: self.calculate('x'))
        self.ui.btn_degree.clicked.connect(lambda: self.calculate('^'))
        self.ui.btn_rem_div.clicked.connect(lambda: self.calculate('%'))

    def add_digit(self, btn_text: str) -> None:
        if self.ui.le.text() == '0':
            self.ui.le.setText(btn_text)
        else:
            self.ui.le.setText(self.ui.le.text() + btn_text)

    def clear_all(self) -> None:
        self.ui.le.setText('0')
        global result
        global znak
        global flag

        result = None
        znak = None
        flag = False
        # self.ui.labelTemp.clear()

    def clear_le(self) -> None:
        self.ui.le.setText('0')

    def add_point(self) -> None:
        if '.' not in self.ui.le.text():
            self.ui.le.setText(self.ui.le.text() + '.')

    @staticmethod
    def remove_trailing_zeros(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n

    def btn_cosinus(self) -> None:
        result = float(self.ui.le.text()) * math.pi / 180
        self.ui.le.setText(str(math.cos(result)))

    def btn_sinus(self) -> None:
        result = float(self.ui.le.text()) * math.pi / 180
        self.ui.le.setText(str(math.cos(result)))

    def calculate(self, btn_text: str) -> None:
        OPERATIONS = {
            '+': add,
            '-': sub,
            'x': mul,
            '/': truediv,
            '%': mod,
            '^': pow,
        }
        global result
        global znak
        global flag

        if flag == False and btn_text != '=':
            result = float(self.ui.le.text())
            znak = btn_text
            self.ui.le.setText('0')
            flag = True
        elif znak and btn_text != '=':
            result = float(OPERATIONS[znak](result, float(self.ui.le.text())))
            self.ui.le.setText(self.remove_trailing_zeros(str(result)))
            znak = btn_text
        elif znak and btn_text == '=':
            result = float(OPERATIONS[znak](result, float(self.ui.le.text())))
            self.ui.le.setText(self.remove_trailing_zeros(str(result)))
            znak = None

    def backspace(self) -> None:
        entry = self.ui.le.text()

        if len(entry) != 1:
            if len(entry) == 2 and '-' in entry:
                self.ui.le.setText('0')
            else:
                self.ui.le.setText(entry[:-1])
        else:
            self.ui.le.setText('0')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())

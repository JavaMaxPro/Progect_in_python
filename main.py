import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from design import Ui_MainWindow


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

        # actiond
        self.ui.btn_clear.clicked.connect(lambda: self.clear_all())
        self.ui.btn_CE.clicked.connect(lambda: self.clear_le())

    def add_digit(self, btn_text: str) -> None:
        if self.ui.le.text() == '0':
            self.ui.le.setText(btn_text)
        else:
            self.ui.le.setText(self.ui.le.text() + btn_text)

    def clear_all(self) -> None:
        self.ui.le.setText('0')
        self.ui.labelTemp.clear()

    def clear_le(self) -> None:
        self.ui.le.setText('0')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.show()

    sys.exit(app.exec())

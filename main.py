import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QPushButton

from ui.base_qt_ui.ui_graph import Ui_Graph


class Graph(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_Graph()
        self.ui.setupUi(self)
        self.buttons = []
        self.end = 0
        self.level = 0
        self.form_button()
        self.ui.button_reset.clicked.connect(self.buttons_reset)

    def change_button_color(self):
        button = app.focusWidget()  # Получаем кнопку, на которую нажали
        if button.palette().button().color().name() == '#ffffff':
            button.setStyleSheet("background-color: black")
        else:
            button.setStyleSheet("background-color: white")
        self.draw_hor_line(button.objectName())

    def buttons_reset(self):
        for i in range(1320):
            self.buttons[i].setStyleSheet(f"background-color: white")
        self.end = 0
        self.level = 0

    def draw_hor_line(self, name: str):
        number = int(name[-4:])
        col = number % 220
        row = number // 220
        if self.end < col:
            for i in range(self.end, col):
                self.buttons[i + row * 220].setStyleSheet("background-color: black")
            if self.level > row:
                for j in range(row, self.level):
                    self.buttons[j*220 + self.end].setStyleSheet("background-color: black")
            elif self.level < row:
                for j in range(self.level, row):
                    self.buttons[j*220 + self.end].setStyleSheet("background-color: black")
            self.end = col
            self.level = row

    def form_button(self):
        for row in range(6):
            for col in range(220):
                button = QPushButton(f"", self)
                button.setGeometry(10 + 5 * col, 10 + 5 * row, 5, 5)
                button.setObjectName(f'button{str(col + 220 * row).zfill(4)}')
                button.setStyleSheet(f"background-color: white")
                button.clicked.connect(self.change_button_color)
                self.buttons.append(button)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Graph()
    main.show()
    sys.exit(app.exec())

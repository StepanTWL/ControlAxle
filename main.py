import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QPushButton

from ui.base_qt_ui.ui_graph import Ui_Graph


class Graph(QtWidgets.QMainWindow):

    def __init__(self, color, x, y):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_Graph()
        self.ui.setupUi(self)
        self.buttons = []
        self.end = 0
        self.level = 0
        self.form_button()
        self.ui.button_reset.clicked.connect(self.buttons_reset)
        self.color = color
        self.x_coord = x
        self.y_coord = y
        print(x)
        print(self.x_coord)

    def change_button_color(self):
        button = app.focusWidget()  # Получаем кнопку, на которую нажали
        if button.palette().button().color().name() == '#ff0000':
            button.setStyleSheet("background-color: red")
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
                self.buttons[i + row * 220].setStyleSheet("background-color: red")
            if self.level > row:
                for j in range(row, self.level):
                    self.buttons[j*220 + self.end].setStyleSheet("background-color: red")
            elif self.level < row:
                for j in range(self.level, row):
                    self.buttons[j*220 + self.end].setStyleSheet("background-color: red")
            self.end = col
            self.level = row

    def form_button(self):
        for row in range(6):
            for col in range(220):
                button = QPushButton(f"", self)
                button.setGeometry(self.y_coord + 5 * col, self.x_coord + 5 * row, 5, 5)
                button.setObjectName(f'button{str(col + 220 * row).zfill(4)}')
                button.setStyleSheet(f"background-color: white")
                button.clicked.connect(self.change_button_color)
                self.buttons.append(button)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    graph1 = Graph('red', 10, 10)
    graph2 = Graph('blue', 60, 10)
    graph1.show()
    graph2.show()
    sys.exit(app.exec())

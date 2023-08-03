import sys

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QPushButton, QWidget

from ui.base_qt_ui.ui_graph import Ui_Graph

row_base = 6
col_base = 200
pixel_size = 5


class System(QWidget):
    def __init__(self, color, parent=None):
        super(System, self).__init__(parent)
        self.color = color
        self.buttons = []
        self.end = 0
        self.level = 0
        pushButton_reset = QPushButton('Reset', self)
        pushButton_reset.setGeometry(1010, 0, 50, 30)
        pushButton_reset.clicked.connect(self.buttons_reset)
        self.form_button()

    def form_button(self):
        for row in range(row_base):
            for col in range(col_base):
                button = QPushButton(f"", self)
                button.setGeometry(pixel_size * col, pixel_size * row, pixel_size, pixel_size)
                button.setObjectName(f'button{str(col + col_base * row).zfill(4)}')
                button.setStyleSheet(f"background-color: white")
                button.clicked.connect(self.change_button_color)
                self.buttons.append(button)
        pass

    def change_color(self):
        self.setStyleSheet(f"background-color: {self.color.name()};")

    def change_button_color(self):
        button = app.focusWidget()  # Получаем кнопку, на которую нажали
        if button.palette().button().color().name() != '#ffffff':
            button.setStyleSheet(f"background-color: {self.color.name()};")
        else:
            button.setStyleSheet("background-color: white")
        self.draw_hor_line(button.objectName())

    def draw_hor_line(self, name: str):
        number = int(name[-4:])
        col = number % col_base
        row = number // col_base
        if self.end < col:
            for i in range(self.end, col):
                self.buttons[i + row * col_base].setStyleSheet(f"background-color: {self.color}")
            if self.level > row:
                for j in range(row, self.level):
                    self.buttons[j * col_base + self.end].setStyleSheet(f"background-color: {self.color}")
            elif self.level < row:
                for j in range(self.level, row):
                    self.buttons[j * col_base + self.end].setStyleSheet(f"background-color: {self.color}")
            self.end = col
            self.level = row

    def buttons_reset(self):
        for i in range(col_base * row_base):
            self.buttons[i].setStyleSheet(f"background-color: white")
        self.end = 0
        self.level = 0


class Graph(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Graph()
        self.ui.setupUi(self)
        self.end = 0
        self.level = 0
        self.system1 = System('red')
        self.system1.setParent(self)
        self.system2 = System('blue')
        self.system2.setParent(self)
        self.ui.button_check.clicked.connect(self.buttons_check)

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.system1.setGeometry(60, 10, 1060, 30)
        self.system2.setGeometry(60, 55, 1060, 30)

    def buttons_check(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    graph = Graph()
    graph.show()
    sys.exit(app.exec())

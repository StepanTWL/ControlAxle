import sys

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QPushButton, QWidget

from ui.base_qt_ui.ui_graph import Ui_Graph


class System(QWidget):
    def __init__(self, x, y, color, parent=None):
        super(System, self).__init__(parent)
        self.x = x
        self.y = y
        self.color = color
        self.buttons = []
        self.end = 0
        self.level = 0
        #self.pushButton_reset = QtWidgets.QPushButton('Reset', self)
        #self.pushButton_reset.setGeometry(1070, self.x, 50, 30)
        self.form_button()

    def form_button(self):
        for row in range(6):
            for col in range(200):
                button = QPushButton(f"", self)
                button.setGeometry(self.x + 10 * col, self.y + 10 * row, 10, 10)
                button.setObjectName(f'button{str(col + 200 * row).zfill(4)}')
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
        col = number % 200
        row = number // 200
        if self.end < col:
            for i in range(self.end, col):
                self.buttons[i + row * 200].setStyleSheet("background-color: red")
            if self.level > row:
                for j in range(row, self.level):
                    self.buttons[j*200 + self.end].setStyleSheet("background-color: red")
            elif self.level < row:
                for j in range(self.level, row):
                    self.buttons[j*200 + self.end].setStyleSheet("background-color: red")
            self.end = col
            self.level = row

    def buttons_reset(self):
        for i in range(1200):
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
        self.ui.button1_layout = QtWidgets.QVBoxLayout()
        self.ui.button1_layout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.ui.button1_layout.setSpacing(0)
        self.ui.button1_layout.addLayout(self.ui.button1_layout)
        system1 = System(10, 10, 'red')
        self.ui.button1_layout.addWidget(system1)
        #self.ui.system2 = System(60, 10, 'blue', self)
        self.ui.button_check.clicked.connect(self.buttons_check)


    def buttons_check(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    graph = Graph()
    graph.show()
    sys.exit(app.exec())

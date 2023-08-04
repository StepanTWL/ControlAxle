import sys

from PyQt6 import QtWidgets, QtCore, QtGui
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
        self.dicct = {}
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        pushButton_reset = QPushButton('Reset', self)
        pushButton_reset.setFont(font)
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
        button = app.focusWidget()
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
            for i in range(self.end, col+1):
                if row < 3:
                    row = 0
                    self.buttons[i].setStyleSheet(f"background-color: {self.color}")
                else:
                    row = 5
                    self.buttons[i + (row_base - 1) * col_base].setStyleSheet(f"background-color: {self.color}")
            if self.level != row and self.end != 0:
                for j in range(row_base):
                    self.buttons[j * col_base + self.end].setStyleSheet(f"background-color: {self.color}")
            self.end = col
            self.level = row

    def buttons_reset(self):
        self.get_data()
        for i in range(col_base * row_base):
            self.buttons[i].setStyleSheet(f"background-color: white")
        self.end = 0
        self.level = 0

    def get_data(self):
        for row in range(0, row_base, 5):
            for col in range(col_base):
                if self.buttons[col + row * col_base].palette().button().color().name() != '#ffffff':
                    if col in self.dicct:
                        self.dicct[col] += row // 5 + 1
                    else:
                        self.dicct[col] = row // 5 + 1
        return self.convert_dict_to_str()

    def convert_dict_to_str(self):
        str = ''
        start = None
        end = None
        for key in self.dicct.keys():
            if self.dicct[key] == 1:
                if start == None:
                    start = key
                if key == col_base - 1:
                    end = key
                    str += f'0:{start}-{end},'
            elif self.dicct[key] == 3:
                end = key
                str += f'0:{start}-{end},'
                start = end
                continue
            if self.dicct[key] == 2:
                if start == None:
                    start = key
                if key == col_base - 1:
                    end = key
                    str += f'1:{start}-{end},'
            elif self.dicct[key] == 3:
                end = key
                str += f'1:{start}-{end},'
                start = end
                continue
        self.dicct.clear()
        return str[:-1]





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
        self.system1.setGeometry(60, 40, 1060, 30)
        self.system2.setGeometry(60, 85, 1060, 30)

    def buttons_check(self):
        str1 = self.system1.get_data()
        str2 = self.system2.get_data()
        self.ui.lineEdit.setText(f"red({str1});blue({str2})")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    graph = Graph()
    graph.show()
    sys.exit(app.exec())

import sys

from PyQt6 import QtWidgets, QtGui
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
        self.time = 20
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
                        self.dicct[col] = row // 5
        return self.convert_dict_to_str()
    
    def convert_dict_to_str(self):
        str = ''
        start = None
        end = None
        for key in range(len(self.dicct)):
            if self.dicct[key] == 0:
                if start == None:
                    start = key
                    if key == col_base - 1:
                        str += f'0:{key}:{self.time}µs; '
                if key == col_base - 1:
                    end = key
                    if start == end:
                        str += f'0:{start}:{self.time}µs; '
                    else:
                        str += f'0:{start}-{end}:{self.time}µs; '
            elif self.dicct[key] == 1:
                if start == None:
                    start = key
                    if key == col_base - 1:
                        str += f'1:{key}:{self.time}µs; '
                if key == col_base - 1:
                    end = key
                    if start == end:
                        str += f'1:{start}:{self.time}µs; '
                    else:
                        str += f'1:{start}-{end}:{self.time}µs '
            elif self.dicct[key] == 2:
                if start == None:
                    start = key
                elif key != 0:
                    end = key - 1
                if self.dicct[end] == 0:
                    if start == end:
                        str += f'0:{start}:{self.time}µs; '
                    else:
                        str += f'0:{start}-{end}:{self.time}µs; '
                    if key != col_base - 1:
                        start = key + 1
                elif self.dicct[end] == 1:
                    if start == end:
                        str += f'1:{start}:{self.time}µs; '
                    else:
                        str += f'1:{start}-{end}:{self.time}µs; '
                    if key != col_base - 1:
                        start = key + 1
                str += f'2:{key}; '
        
        self.dicct.clear()
        return str[:-2]
    
    def set_time_step(self, value):
        self.time = value





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
        self.system1.set_time_step(self.ui.spinBox.text())
        self.system2.set_time_step(self.ui.spinBox.text())
        str1 = self.system1.get_data()
        str2 = self.system2.get_data()
        self.ui.textEdit.setText(f"SYS1({str1});SYS2({str2})")
        self.form_mass_data()
    
    def form_mass_data(self):
        pass
    #SYS1(0:0-48:20µs; 2:49; 1:50-125:20µs; 2:126; 0:127-199:20µs);SYS2(0:0-70:20µs; 2:71; 1:72-141:20µs; 2:142; 0:143-199:20µs)
    #SYS1(0:980; 1:2520us; 0:3980);SYS2(0:1420us; 1:2840us; 0:3980us)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    graph = Graph()
    graph.show()
    sys.exit(app.exec())

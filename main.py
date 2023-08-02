import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QPushButton

from ui.base_qt_ui.ui_graph import Ui_Graph


class System(QtWidgets):
    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.buttons = []
        self.ui.pushButton_reset = QtWidgets.QPushButton('Reset', self)
        self.ui.pushButton_reset.setGeometry(1070, 10, 50, 30)
        self.form_button()
        
    
    def form_button(self):
        for row in range(6):
            for col in range(200):
                button = QPushButton(f"", self)
                button.setGeometry(self.x + 5 * col, self.y + 5 * row, 5, 5)
                button.setObjectName(f'button{str(col + 200 * row).zfill(4)}')
                button.setStyleSheet(f"background-color: white")
                button.clicked.connect(self.change_button_color)
                self.buttons.append(button)
    
    def change_color(self):
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.setStyleSheet(f"background-color: {color.name()};")
    

class Graph(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Graph()
        self.ui.setupUi(self)
        self.end = 0
        self.level = 0
        self.system1 = System('red', 10, 10)
        self.system2 = System('blue', 10, 60)
        #self.ui.button_check.clicked.connect(self.buttons_check)

    def change_button_color(self):
        button = app.focusWidget()  # Получаем кнопку, на которую нажали
        if button.palette().button().color().name() == '#ff0000':
            button.setStyleSheet("background-color: red")
        else:
            button.setStyleSheet("background-color: white")
        self.draw_hor_line(button.objectName())

    def buttons_reset(self):
        for i in range(1200):
            self.buttons[i].setStyleSheet(f"background-color: white")
        self.end = 0
        self.level = 0

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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    graph = Graph()
    graph.show()
    sys.exit(app.exec())

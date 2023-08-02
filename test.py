import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

class MyButton(QPushButton):
    def __init__(self, x, y, parent):
        super().__init__("", parent)
        self.setGeometry(x, y, 10, 10)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример кнопок PyQt6")
        self.setGeometry(100, 100, 400, 200)

        self.init_ui()

    def init_ui(self):
        # Создаем первую кнопку через класс MyButton1
        button1 = MyButton(50, 50, self)

        # Создаем вторую кнопку через класс MyButton2
        button2 = MyButton(200, 100, self)

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton
import sys

class MyCustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a label
        self.label = QLabel("Hello, I am a custom widget label!", self)
        self.label.setGeometry(10, 10, 200, 30)  # Set the position and size of the label using absolute coordinates

        # Create a QPushButton and connect its clicked signal to the on_button_click method
        self.button = QPushButton("Click Me!", self)
        self.button.setGeometry(10, 50, 100, 30)  # Set the position and size of the button using absolute coordinates
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("Button clicked!")

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Window")
        self.setGeometry(100, 100, 400, 300)

        # Create the custom widget
        self.custom_widget = MyCustomWidget()
        self.custom_widget.setParent(self)  # Set the main window as the parent of the custom widget

    def resizeEvent(self, event):
        super().resizeEvent(event)

        # Set the geometry of the custom widget when the main window is resized
        self.custom_widget.setGeometry(100, 100, 200, 100)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec())

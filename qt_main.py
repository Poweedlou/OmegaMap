from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys
from image_coords import get_bytes_image
from scale import scale


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
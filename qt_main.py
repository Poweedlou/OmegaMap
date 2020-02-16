from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
import sys
from image_coords import get_bytes_image
from scale import scale
from map import Map


class Window(QWidget):
    def __init__(self, ):
        self.map = Map(input('Enter start point\n'))
        super().__init__()
        self.initUI()

    def initUI(self):
        self.vlo = QVBoxLayout()
        self.setLayout(self.vlo)
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText('Enter place')
        hlo = QHBoxLayout()
        self.vlo.addLayout(hlo)
        hlo2 = QHBoxLayout()
        b1 = QPushButton("Find!")
        hlo.addWidget(self.lineEdit)
        hlo.addWidget(b1)
        self.vlo.addWidget(self.map)
        self.vlo.addLayout(hlo2)
        b1.clicked.connect(self.findPlace)
        mapbtn = QPushButton("map")
        satbtn = QPushButton("sat")
        hybbtn = QPushButton("hyb")
        mapbtn.clicked.connect(self.changeMap)
        satbtn.clicked.connect(self.changeMap)
        hybbtn.clicked.connect(self.changeMap)
        hlo2.addWidget(mapbtn)
        hlo2.addWidget(satbtn)
        hlo2.addWidget(hybbtn)

    def changeMap(self):
        a = self.sender().text()
        if a == 'hyb':
            a = 'sat,skl'
        self.map.changeMap(a)

    def findPlace(self):
        self.map.findPlace(self.lineEdit.text())
        self.map.loadMap()

    #def 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QCheckBox
import sys
from image_coords import get_bytes_image
from map import Map


class Window(QWidget):
    def __init__(self, ):
        self.map = Map(input('Enter start point\n'))
        self.adress, self.code = None, None
        super().__init__()
        self.initUI()

    def initUI(self):
        self.vlo = QVBoxLayout()
        self.cb = QCheckBox('postal_code')
        self.adressLabel = QLabel()
        hlo3 = QHBoxLayout()
        self.setLayout(self.vlo)
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText('Enter place')
        hlo = QHBoxLayout()
        self.vlo.addLayout(hlo)
        hlo2 = QHBoxLayout()
        b1 = QPushButton("Find!")
        hlo.addWidget(self.lineEdit)
        hlo.addWidget(b1)
        hlo3.addWidget(self.adressLabel)
        hlo3.addWidget(self.cb)
        self.vlo.addLayout(hlo3)
        self.vlo.addWidget(self.map)
        self.vlo.addLayout(hlo2)
        b1.clicked.connect(self.findPlace)
        mapbtn = QPushButton("map")
        satbtn = QPushButton("sat")
        hybbtn = QPushButton("hyb")
        flush = QPushButton("Сброс")
        mapbtn.clicked.connect(self.changeMap)
        satbtn.clicked.connect(self.changeMap)
        hybbtn.clicked.connect(self.changeMap)
        hlo2.addWidget(mapbtn)
        hlo2.addWidget(satbtn)
        hlo2.addWidget(hybbtn)
        hlo2.addWidget(flush)
        self.cb.clicked.connect(self.addAdress)
        flush.clicked.connect(self.flush)
    
    def flush(self):
        self.map.flush()
        self.adress, self.code = None, None
        self.addAdress()

    def changeMap(self):
        a = self.sender().text()
        if a == 'hyb':
            a = 'sat,skl'
        self.map.changeMap(a)

    def findPlace(self):
        self.adress, self.code = self.map.findPlace(self.lineEdit.text())
        self.map.loadMap()
        self.addAdress()
    
    def addAdress(self):
        t = ''
        if self.adress is not None:
            t += self.adress
        if self.cb.isChecked():
            if self.code is not None:
                t += ', ' + self.code
        self.adressLabel.setText(t)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
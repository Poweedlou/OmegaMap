from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QCheckBox
import sys
from image_coords import get_bytes_image
from map import Map


modes = {
    "Схема": 'map',
    "Спутник": 'sat',
    "Гибрид": 'sat,skl'
}


class Window(QWidget):
    def __init__(self):
        self.map = Map('Череповец')
        self.adress, self.code = None, None
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(670, 570)
        self.vlo = QVBoxLayout()
        self.cb = QCheckBox('Почтовый код')
        self.adressLabel = QLabel()
        hlo3 = QHBoxLayout()
        self.setLayout(self.vlo)
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText('Введите место')
        hlo = QHBoxLayout()
        self.vlo.addLayout(hlo)
        hlo2 = QHBoxLayout()
        b1 = QPushButton("Искать!")
        hlo.addWidget(self.lineEdit)
        hlo.addWidget(b1)
        hlo3.addWidget(self.adressLabel)
        hlo3.addWidget(self.cb)
        self.vlo.addLayout(hlo3)
        self.vlo.addWidget(self.map)
        self.vlo.addLayout(hlo2)
        b1.clicked.connect(self.findPlace)
        mapbtn = QPushButton("Схема")
        satbtn = QPushButton("Спутник")
        hybbtn = QPushButton("Гибрид")
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
        self.map.changeMap(modes[a])

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
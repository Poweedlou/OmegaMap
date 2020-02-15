from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from scale import scale
from image_coords import get_bytes_image


keys = {
    16777235: (0, 1),
    16777237: (0, -1),
    16777234: (-1, 0),
    16777236: (1, 0)
}
spn_keys = {
    16777238: -1,
    16777239: 1
}


class Map(QLabel):
    def __init__(self, start):
        super().__init__()
        self.findPlace(start)
        self.mode = 'map'
        self.dots = []
        self.save()
        self.setFixedSize(650, 450)
        self.loadMap()

    def findPlace(self, place):
        self.save()
        self.coords, self.spn = scale(place)

    def save(self):
        self.prev_coords = self.coords
        self.prev_spn = self.spn
        self.prev_mode = self.mode

    def go_back(self):
        self.coords = self.prev_coords
        self.spn = self.prev_spn
        self.mode = self.prev_mode

    def loadMap(self):
        a = get_bytes_image(self.coords, self.spn, self.mode)
        if a is None:
            self.go_back()
        else:
            self.img = QPixmap()
            self.img.loadFromData(a)
            self.setPixmap(self.img)

    def moveMap(self, dir_):
        self.save()
        dx, dy = dir_
        self.coords[0] += dx * self.spn
        self.coords[1] += dy * self.spn
        self.loadMap()

    def changeSpn(self, ds):
        self.save()
        self.spn *= 2**ds
        self.loadMap()

    def changeMap(self, mode):
        self.save()
        self.mode = mode
        self.loadMap()

    def mousePressEvent(self, ev):
        b = ev.button()
        if b == 1:
            self.setFocus()
        if b == 2:
            pass

    def keyPressEvent(self, event):
        key = event.key()
        try:
            self.moveMap(keys[key])
        except:
            try:
                self.changeSpn(spn_keys[key])
            except:
                pass

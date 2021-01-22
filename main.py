import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)
        self.setFixedSize(600, 500)
        self.f = False
        self.setWindowTitle('Git и желтые окружности')
        self.btn.clicked.connect(self.paint)

    def paint(self):
        self.f = True
        self.repaint()

    def paintEvent(self, event):
        if self.f:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(15):
            r = random.randint(20, 80)
            x = random.randint(40, 540)
            y = random.randint(40, 440)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())

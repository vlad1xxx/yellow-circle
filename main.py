from PyQt5 import uic
import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.should_draw = False
        self.initUI()

    def initUI(self):
        self.draw_btn.clicked.connect(self.redraw)

    def redraw(self):
        self.should_draw = True
        self.update()

    def paintEvent(self, event):
        if self.should_draw:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_circle(self.qp)
            self.qp.end()
        self.should_draw = False

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        width = randint(0, 800)
        height = randint(0, 600)
        radius = randint(10, 200)
        qp.drawEllipse(width, height, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MyWidget()
    mw.show()
    sys.exit(app.exec())
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_dawing_window3(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Github Drawing")
        self.tako = QPixmap("images/tako.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.drawPixmap(QRect(200, 100, 320, 320), self.tako)

        p.setPen(QColor(0, 0, 255)) 
        p.setBrush(QColor(0, 255, 255))
        p.drawRect(50, 50, 100, 100)

        p.end()


def main():
    app = QApplication(sys.argv)
    w = Simple_dawing_window3()
    w.show()

    return app.exec()
    
if __name__ == "__main__":
    sys.exit(main())
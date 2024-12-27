import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Github Drawing")
        self.rabbit = QPixmap("images/buffalo.jpg")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255,127,0))

        p.drawPolygon(
            [QPoint(50,200), QPoint(150,200), QPoint(100,400)]
        )

        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()


class Simple_drawing_window2(QWidget) :
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Github Drawing")
        self.duck = QPixmap("images/duck.png")
        self.setGeometry(100,100,400,400)

    def paintEvent(self , e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawEllipse(100,100,200,200)
        

        p.drawPixmap(QRect(200,100,320,320),self.duck)

class Simple_drawing_window3(QWidget):
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


def main() :
    app = QApplication(sys.argv)
    
    x = Simple_drawing_window1()
    w = Simple_drawing_window2()
    z = Simple_drawing_window3()
    x.show()
    w.show()
    z.show()

    return app.exec()

if __name__ == "__main__" :
    sys.exit(main())


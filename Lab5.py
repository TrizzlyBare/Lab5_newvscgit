import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

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


def main() :
    app = QApplication(sys.argv)
    
    w = Simple_drawing_window2()
    w.show()

    return app.exec()

if __name__ == "__main__" :
    sys.exit(main())


import sys
import random
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.can_paint = False
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.can_paint = True
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.can_paint:
            self.draw(qp)
        qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        a = random.randint(1, 80)
        qp.drawEllipse(random.randint(1, 600), random.randint(1, 600), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
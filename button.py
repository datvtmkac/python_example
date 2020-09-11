#!usr/bin/env python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super(App, self).__init__()
        self.title = 'button'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('press', self)
        button.setToolTip('This is an example button')
        button.move(50,70)
        button.clicked.connect(self.on_click)

        button1 = QPushButton('push', self)
        button1.move(150,70)
        button1.clicked.connect(self.on_click_2)
        
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button pressed')

    def on_click_2(self):
        print('PyQT5 button pushed')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

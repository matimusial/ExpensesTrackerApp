from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.loadBaseCalcUI()
        self.show()

    def loadBaseCalcUI(self):
        uic.loadUi("untitled.ui", self)

app = QApplication(sys.argv)
window = App()
app.exec_()
#! /usr/bin/python3

from PyQt6 import QtWidgets 
from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QVBoxLayout, QPushButton

from Models.LiquidCalc import LiquidCalc

from Views.Widgets.CustomWidgets import VolumeGroup, ResultGroup
import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Розрахунок температури рідини при змішуванні")
        self.setMinimumSize(600, 380)
        self.centerWindow()
        self._initUI()

    def _initUI(self):
        """ user interface initializing"""
        ico = QIcon("Img/logo.png")
        self.setWindowIcon(ico)
        main_layout = QVBoxLayout()
        self._volume1 = VolumeGroup("Ємність №1:")
        self._volume2 = VolumeGroup("Ємність №2:")

        calc_btn = QPushButton("Розрахувати")
        calc_btn.setMaximumWidth(200)
        calc_btn.clicked.connect(self.calcResult)
        self.resultLbl = ResultGroup('Результат:')

        main_layout.addWidget(self._volume1)
        main_layout.addWidget(self._volume2)
        main_layout.addWidget(calc_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(self.resultLbl, alignment=Qt.AlignmentFlag.AlignHCenter)

        main_layout.addStretch(40)
        main_layout.setSpacing(30)
        self.setLayout(main_layout)

    def calcResult(self):
        calc = LiquidCalc(self._volume1.getVolume(), self._volume1.getTemperature(),
                          self._volume2.getVolume(), self._volume2.getTemperature())
        self.resultLbl.setText(f"{calc.getResultVolume():.1f} л температурою {calc.getResultTemperature():.1f} °C")

    def event(self, e) -> QtWidgets.QWidget.event:
        """ hotkey handling """
        if e.type() == QEvent.Type.WindowDeactivate:
            self.setWindowOpacity(0.85)
        elif e.type() == QEvent.Type.WindowActivate:
            self.setWindowOpacity(1)
        elif e.type() == QEvent.Type.KeyPress and e.key() == Qt.Key.Key_Escape:
            self.close()
        return QtWidgets.QWidget.event(self, e)

    def centerWindow(self):
        """ centering the main window at the center of the screen """
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    """ start program function """
    app = QtWidgets.QApplication(sys.argv)
    with open("style.css", "r") as file:
        app.setStyleSheet(file.read())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
#! /usr/bin/python3

from PyQt6 import QtWidgets 
from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QStyleFactory, QMenu, QVBoxLayout, QGroupBox, QHBoxLayout, QLabel, QGridLayout, QLineEdit, \
    QPushButton

from Views.Widgets.CustomWidgets import IntSpinBox
# from Views.Widgets.Translator import UkrainianTranslator
# from Project import Project, Settings
# from ProjectTypes import Theme
import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Розрахунок температури рідини при змішуванні")
        self.setMinimumSize(600, 340)
        self.centerWindow()
        self._initUI()

    def _initUI(self):
        """ user interface initializing"""
        ico = QIcon("Img/logo.png")
        self.setWindowIcon(ico)
        main_layout = QVBoxLayout()
        volume1 = QGroupBox("Ємність №1")
        volume1.setMaximumHeight(130)
        volume1_layout = QGridLayout()
        volume1.setLayout(volume1_layout)

        labelV1 = QLabel("Об'єм (л)")
        labelT1 = QLabel("Температура (°C)")
        editV1 = IntSpinBox()
        editT1 = IntSpinBox()
        volume1_layout.addWidget(labelV1, 0, 0, Qt.AlignmentFlag.AlignCenter)
        volume1_layout.addWidget(labelT1, 0, 1, Qt.AlignmentFlag.AlignCenter)
        volume1_layout.addWidget(editV1, 1, 0)
        volume1_layout.addWidget(editT1, 1, 1)

        volume2 = QGroupBox("Ємність №2")
        volume2.setMaximumHeight(130)
        volume2_layout = QGridLayout()
        volume2.setLayout(volume2_layout)

        labelV2 = QLabel("Об'єм (л)")
        labelT2 = QLabel("Температура (°C)")
        editV2 = IntSpinBox()
        editT2 = IntSpinBox()
        volume2_layout.addWidget(labelV2, 3, 0, Qt.AlignmentFlag.AlignCenter)
        volume2_layout.addWidget(labelT2, 3, 1, Qt.AlignmentFlag.AlignCenter)
        volume2_layout.addWidget(editV2, 4, 0)
        volume2_layout.addWidget(editT2, 4, 1)

        volume1_layout.setContentsMargins(100, 20, 100, 20)
        volume1_layout.setHorizontalSpacing(100)
        volume2_layout.setContentsMargins(100, 20, 100, 20)
        volume2_layout.setHorizontalSpacing(100)

        calc_btn = QPushButton("Розрахувати")
        calc_btn.setMaximumWidth(200)

        result_lbl = QLabel("70 літрів температурою 30°C")
        result_lbl.setObjectName('orange')

        main_layout.addWidget(volume1)
        main_layout.addWidget(volume2)
        main_layout.addWidget(calc_btn, alignment = Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(result_lbl, alignment = Qt.AlignmentFlag.AlignCenter)

        self.setLayout(main_layout)

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
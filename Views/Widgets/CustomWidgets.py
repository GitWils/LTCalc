from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt

class IntSpinBox(QtWidgets.QSpinBox):
    """ Spinbox widget for int numbers """
    def __init__(self, readonly=False, changedFunc=None) -> None:
        super().__init__()
        self.setValue(0)
        self.setMaximum(100000)
        self.setReadOnly(readonly)
        if changedFunc: self.textChanged.connect(changedFunc)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

class FloatSpinBox(QtWidgets.QDoubleSpinBox):
    """ Spinbox widget for float numbers """
    def __init__(self, readonly=False, changedFunc=None):
        super().__init__()
        self.setValue(1)
        self.setMaximum(100000)
        self.setReadOnly(readonly)
        self.setDecimals(2)
        if changedFunc: self.textChanged.connect(changedFunc)

class LineEdit(QtWidgets.QLineEdit):
    """ LineEdit widget with custom parameters """
    def __init__(self, text='', readonly=False, changedFunc=None) -> None:
        super().__init__()
        self.setReadOnly(readonly)
        self.setText(text)
        if changedFunc: self.textChanged.connect(changedFunc)

class Note(QtWidgets.QTextEdit):
    def __init__(self) -> None:
        super().__init__()
        self.setMaximumHeight(100)

class VolumeGroup(QtWidgets.QGroupBox):
    """ QGroupBox widget with volume and temperature edit boxes """
    def __init__(self, title=''):
        super().__init__()
        self.setTitle(title)
        volume_layout = QtWidgets.QGridLayout()
        self.setLayout(volume_layout)

        labelV = QtWidgets.QLabel("Об'єм (л)")
        labelT = QtWidgets.QLabel("Температура (°C)")
        self._editV = IntSpinBox()
        self._editT = IntSpinBox()
        volume_layout.addWidget(labelV, 0, 0, Qt.AlignmentFlag.AlignCenter)
        volume_layout.addWidget(labelT, 0, 1, Qt.AlignmentFlag.AlignCenter)
        volume_layout.addWidget(self._editV, 1, 0)
        volume_layout.addWidget(self._editT, 1, 1)

        volume_layout.setContentsMargins(100, 20, 100, 20)
        volume_layout.setHorizontalSpacing(100)

    def getVolume(self):
        """ returns volume value from spinbox """
        return self._editV.value()

    def getTemperature(self):
        """ returns temperature value from spinbox """
        return self._editT.value()

class ResultGroup(QtWidgets.QGroupBox):
    """ QGroupBox widget for result values showing """
    def __init__(self, title='') -> None:
        super().__init__()
        self.setTitle(title)
        self._labelResult = QtWidgets.QLabel()
        self._labelResult.setObjectName('orange')
        self._labelResult.setMinimumWidth(380)
        result_layout = QtWidgets.QVBoxLayout()
        result_layout.addWidget(self._labelResult, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(result_layout)
        result_layout.setContentsMargins(100, 20, 100, 20)

    def setText(self, text) -> None:
        self._labelResult.setText(text)
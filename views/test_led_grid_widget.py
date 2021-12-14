from PySide2.QtWidgets import QWidget, QGridLayout, QHBoxLayout


class TestLedGridWidget(QWidget):
    def __init__(self, parent: QWidget = None):
        super(TestLedGridWidget, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        grid_layout = QHBoxLayout()

        self.leds = [QWidget() for i in range(10)]
        for led in self.leds:
            led.setStyleSheet('border: 1px solid black; background-color:white')
            led.setFixedSize(20, 20)
            grid_layout.addWidget(led)

        self.leds[3].setStyleSheet('border: 1px solid black; background-color:green')
        self.setLayout(grid_layout)

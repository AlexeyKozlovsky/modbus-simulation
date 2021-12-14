from PySide2.QtWidgets import QWidget, QGroupBox, QGridLayout, QLabel


class VoltageManagerView(QGroupBox):
    def __init__(self, parent: QWidget = None):
        super(VoltageManagerView, self).__init__("БПК-1", parent)
        self._init_ui()

    def _init_ui(self):
        main_layout = QGridLayout()

        self.voltage_indicator = QWidget()
        self.voltage_indicator.setFixedSize(20, 20)
        self.voltage_indicator.setStyleSheet('border: 1px solid black; background-color: white')

        main_layout.addWidget(self.voltage_indicator, 0, 0, 1, 1)
        main_layout.addWidget(QLabel("Подключен"), 0, 1, 1, 1)
        self.setLayout(main_layout)

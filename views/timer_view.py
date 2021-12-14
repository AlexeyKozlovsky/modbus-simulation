from PySide2.QtWidgets import QWidget, QGridLayout, QLabel, QGroupBox


class TimerView(QGroupBox):
    def __init__(self, parent: QWidget = None):
        super(TimerView, self).__init__("Т8-31", parent)
        self._init_ui()

    def _init_ui(self):
        main_layout = QGridLayout()
        self.voltage_indicator = QWidget()
        self.voltage_indicator.setFixedSize(20, 20)
        self.voltage_indicator.setStyleSheet('border: 1px solid black; background-color: white')

        main_layout.addWidget(self.voltage_indicator, 0, 0, 1, 1)
        main_layout.addWidget(QLabel("Питание"), 0, 1, 1, 5)

        main_layout.addWidget(QLabel("Каналы"), 1, 0, 1, 9)

        self.channel_indicators = [QWidget() for i in range(8)]
        self.channel_inv_indicators = [QWidget() for i in range(8)]
        self.channel_delays = [QLabel("0") for i in range(8)]
        self.channel_periods = [QLabel("0") for i in range(8)]
        for i, channel_indicator in enumerate(self.channel_indicators):
            channel_name = f'{["A", "B"][i // 4]}{i % 4 + 1}'
            channel_indicator.setStyleSheet('border: 1px solid black; background-color: white')
            channel_indicator.setFixedSize(20, 20)

            self.channel_inv_indicators[i].setFixedSize(20, 20)
            self.channel_inv_indicators[i].setStyleSheet('border: 1px solid black; background-color: white')

            main_layout.addWidget(QLabel(channel_name), 2, i, 1, 1)

            channel_indicators_layout = QGridLayout()
            channel_indicators_layout.addWidget(QLabel("ON"), 0, 0, 1, 1)
            channel_indicators_layout.addWidget(channel_indicator, 1, 0, 1, 1)
            channel_indicators_layout.addWidget(QLabel("INV"), 0, 1, 1, 1)
            channel_indicators_layout.addWidget(self.channel_inv_indicators[i], 1, 1, 1, 1)

            main_layout.addLayout(channel_indicators_layout, 3, i, 1, 1)
            main_layout.addWidget(QLabel("Период"), 4, i, 1, 1)
            main_layout.addWidget(self.channel_periods[i], 5, i, 1, 1)
            main_layout.addWidget(QLabel("Задержка"), 6, i, 1, 1)
            main_layout.addWidget(self.channel_delays[i], 7, i, 1, 1)

        self.setLayout(main_layout)

    def change_channel_indicator(self, channel_num: int, status: bool):
        if status:
            color = 'green'
        else:
            color = 'white'

        self.channel_indicators[channel_num].setStyleSheet(f'border: 1px solid black; background-color: {color}')

    def change_channel_inv_indicator(self, channel_num: int, status: bool):
        self.channel_inv_indicators[channel_num].setStyleSheet(f'border: 1px solid black; background-color: {"green" if status else "white"}')

    def change_channel_delay(self, channel_num: int, delay: int):
        self.channel_delays[channel_num].setText(delay)

    def change_channel_period(self, channel_num: int, period: int):
        self.channel_periods[channel_num].setText(period)

    def switch(self, on: bool):
        self.voltage_indicator.setStyleSheet(f'border: 1px solid black; background-color: {"green" if on else "white"}')
        if not on:
            for i in range(8):
                self.change_channel_inv_indicator(i, False)
                self.change_channel_indicator(i, False)

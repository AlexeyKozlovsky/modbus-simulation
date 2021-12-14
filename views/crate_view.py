from pyModbusTCP.server import ModbusServer, DataBank
from PySide2.QtWidgets import QWidget, QGroupBox, QLabel, QVBoxLayout
from PySide2.QtCore import QThread

from services.listener import Worker
from views.voltage_manager_view import VoltageManagerView
from views.timer_view import TimerView


def counts_to_value(lsb, msb):
    value = ((msb << 16) | lsb) * 25
    return value


class CrateView(QGroupBox):
    def __init__(self, name: str, parent: QWidget = None):
        super(CrateView, self).__init__(name, parent)
        self.server = ModbusServer('0.0.0.0', port=4001, no_block=True)
        self._init_ui()

        self.listener = Worker()
        self.thread = QThread()

        self.listener.moveToThread(self.thread)
        self.listener.update.connect(self.update_values)
        self.thread.started.connect(self.listener.update_cycle)
        self.listener.finished.connect(self.thread.finished)

    def _init_ui(self):
        main_layout = QVBoxLayout()

        self.voltage_manager_view = VoltageManagerView()
        self.timer_view = TimerView()

        main_layout.addWidget(self.voltage_manager_view)
        main_layout.addWidget(self.timer_view)
        main_layout.addStretch(1)

        self.setLayout(main_layout)

    def start_server(self):
        self.server.start()
        self.thread.start()

    def stop_server(self):
        self.thread.quit()
        self.server.stop()

    def update_values(self):
        print('UPDATING')
        voltage_status = DataBank.get_words(28, 1)[0]

        channel_statuses = DataBank.get_words(32, 8)[::2]
        channel_statuses.extend(DataBank.get_words(41, 8)[::2])

        channel_inv_statuses = DataBank.get_words(33, 8)[::2]
        channel_inv_statuses.extend(DataBank.get_words(42, 8)[::2])

        registers = DataBank.get_words(0, 32)
        channel_delays_msb = registers[::4]
        channel_delays_lsb = registers[1::4]
        channel_widths_msb = registers[2::4]
        channel_widths_lsb = registers[3::4]

        self.timer_view.switch(voltage_status)

        if voltage_status:
            for i, channel_status in enumerate(channel_statuses):
                self.timer_view.change_channel_indicator(i, channel_status)

            for i, channel_inv_status in enumerate(channel_inv_statuses):
                self.timer_view.change_channel_inv_indicator(i, channel_inv_status)

            for i, channel_delay in enumerate(channel_delays_msb):
                value = counts_to_value(channel_delay, channel_delays_lsb[i])
                self.timer_view.change_channel_delay(i, str(value))

            for i, channel_width in enumerate(channel_widths_msb):
                value = counts_to_value(channel_width, channel_widths_lsb[i])
                self.timer_view.change_channel_width(i, str(value))

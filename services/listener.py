import time

from PySide2.QtCore import QThread, QObject, Signal, Slot


class Worker(QObject):
    finished = Signal()
    intReady = Signal(int)
    update = Signal()

    def update_cycle(self):
        while True:
            self.update.emit()
            time.sleep(0.5)

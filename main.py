import sys

from PySide2.QtWidgets import QApplication

from views.crate_view import CrateView


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CrateView("Крейт 1")
    widget.start_server()
    widget.show()
    app.exec_()

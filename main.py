from PyQt6.QtWidgets import QApplication

from controller import Controller

if __name__ == '__main__':
    import sys
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())

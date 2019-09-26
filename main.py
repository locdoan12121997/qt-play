from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import test

class ExampleApp(QMainWindow, test.Ui_CinemaUI):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

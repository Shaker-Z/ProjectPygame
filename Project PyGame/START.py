from PyQt5.QtGui import QPixmap, QPalette, QBrush, QIcon
from Qt.ui_startwind import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import subprocess, sys


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pixm = QPixmap('data/objects/bg_grasslands.png').scaled(self.width(), self.height())
        self.palette = QPalette()
        self.palette.setBrush(10, QBrush(self.pixm))
        self.setPalette(self.palette)
        self.setWindowIcon(QIcon('data/enemys/kolobok.png'))
        self.startButton.clicked.connect(self.start)
        self.quitButton.clicked.connect(self.quit)

    def start(self):
        self.close()
        subprocess.call(['python', 'level_select.py'], shell=True)

    def quit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

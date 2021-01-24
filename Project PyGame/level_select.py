from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QIcon
from Qt.ui_levelselect import Ui_MainWindow
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
        for bt in self.buttonGroup.buttons():
            if 1 <= int(bt.objectName()[bt.objectName().find("_") + 1:]) <= 2:
                bt.setIcon(QIcon(f'data/objects/box_{bt.objectName()[bt.objectName().find("_")+1:]}.png'))
                bt.setIconSize(QSize(bt.size()))
            else:
                bt.setIcon(QIcon('data/objects/boxEmpty.png'))
                bt.setIconSize(QSize(bt.size()))
        self.buttonGroup.buttonClicked.connect(self.start)

    def start(self, button):
        if 1 <= int(button.objectName()[button.objectName().find("_") + 1:]) <= 2:
            with open('lvl.txt', mode='wt', encoding='utf8') as lvl:
                lvl.write(button.objectName()[button.objectName().find('_')+1:])
            self.close()
            subprocess.call(['python', 'game.py'], shell=True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
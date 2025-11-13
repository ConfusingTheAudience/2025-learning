# PyQt5 Digital clock

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
# from PyQt5.QtGui import QFont, QFontDatabase = this is for font

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Digital clock')
        self.setGeometry(800, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet('font-size: 150px;'
                                      'font-family: Arial;'
                                      'color: #26ff00')
        self.setStyleSheet('background-color: #000')

        # if we want our font
        # font_id = QFontDatabase.addApplicationFont('DS-DIGIT.TTF')
        # font_family = QFontDatabase.addApplicationFontFamilies(font_id)[0]
        # my_font = QFont(font_family, 150)
        # self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString('hh:mm:ss AP')
        self.time_label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
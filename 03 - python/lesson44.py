# PyQt5

# 69. PyQt5 CSS styles

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # since we are using layout manager we don't need to put
        # the button to self (to the window)
        self.button1 = QPushButton('#1')
        self.button2 = QPushButton('#2')
        self.button3 = QPushButton('#3')
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        # we need to do it if we want to use setStyleSheet by object name with triple quotes
        self.button1.setObjectName('button1')
        self.button2.setObjectName('button2')
        self.button3.setObjectName('button3')

        # instead
        # self.button1.setStyleSheet('')
        # we do, with triple qoutes
        self.setStyleSheet('''
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px
            }
            QPushButton#button1{
                background-color: #ff6666;        
            }
            QPushButton#button2{
                background-color: #82ffa3;        
            }
            QPushButton#button3{
                background-color: #30a2ff;        
            }
            QPushButton#button1:hover{
                background-color: #ff9999;;        
            }
            QPushButton#button2:hover{
                background-color: #b8ffc8;        
            }
            QPushButton#button3:hover{
                background-color: #7cc8ff;        
            }
        ''')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

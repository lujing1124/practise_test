from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui.Ui_main_window import Ui_MainWindow
from net_assist_widget import NetAssistWidget
from serial_assist_widget import SerialAssistWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        
    def init_ui(self):
        w = NetAssistWidget(self)
        s = SerialAssistWidget(self)
        self.ui.tabWidget.addTab(w,"网络助手")
        self.ui.tabWidget.addTab(s,"串口助手")
        self.ui.tabWidget.setCurrentIndex(1)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()

    w.show()
    sys.exit(app.exec_())
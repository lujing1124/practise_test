from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui.Ui_serial_assist_widget import Ui_SerialAssistWidget
import sys

class SerialAssistWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.ui = Ui_SerialAssistWidget()
        self.ui.setupUi(self)
        self.init_ui()
        
    def init_ui(self):
        pass
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SerialAssistWidget()

    w.show()
    sys.exit(app.exec_())
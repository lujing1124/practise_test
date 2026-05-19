from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui.Ui_net_assist_widget import Ui_NetAssistWidget
import sys

class NetAssistWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.ui = Ui_NetAssistWidget()
        self.ui.setupUi(self)
        self.init_ui()
        
    def init_ui(self):
        pass
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = NetAssistWidget()

    w.show()
    sys.exit(app.exec_())
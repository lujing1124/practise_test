from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("jennyFunc")
w.resize(1280,960)  #窗口大小
icon = QIcon("icon.png")
w.setWindowIcon(icon)
w.show()
w.setToolTip("气泡提示")
exec_code = app.exec_()
print(exec_code)
sys.exit(exec_code)
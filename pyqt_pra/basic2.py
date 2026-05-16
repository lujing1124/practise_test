from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("jennyFunc")


# label = QLabel(w)
label = QLabel()
pixmap = QPixmap("./4.jpg")
label.setPixmap(pixmap)
w.resize(1280,960)  #窗口大小
# label.setText("第一个文本")
label.setParent(w)









w.show()


sys.exit(app.exec_())
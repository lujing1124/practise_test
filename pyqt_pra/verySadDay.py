from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton
import sys

def click_func():
    print('sendding...')

def init_widget(w: QWidget):
    layout = QHBoxLayout()  #水平布局
    
    btn1 = QPushButton("按钮1")
    btn2 = QPushButton("按钮2")
    btn3 = QPushButton("按钮3")
    btn4 = QPushButton("按钮4")

    layout.addWidget(btn1)
    layout.addWidget(btn2)
    layout.addWidget(btn3)
    layout.addWidget(btn4)
 
    w.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("jennyFunc")
    w.resize(640,480)  #窗口大小
    
    # init_widget(w)

    w.show()
    sys.exit(app.exec_())
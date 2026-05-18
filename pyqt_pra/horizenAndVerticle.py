from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton
import sys

def click_func():
    print('sendding...')

def init_widget(w: QWidget):
    root_layout = QHBoxLayout()
    w.setLayout(root_layout)

    col1_layout = QVBoxLayout()
    col1_layout.addWidget(QPushButton("1"))

    col2_layout = QVBoxLayout()
    col2_layout.addWidget(QPushButton("1"))
    col2_layout.addWidget(QPushButton("2"))

    col3_layout = QVBoxLayout()
    col3_layout.addWidget(QPushButton("1"))
    col3_layout.addWidget(QPushButton("2"))
    col3_layout.addWidget(QPushButton("3"))
    
    root_layout.addLayout(col1_layout)
    root_layout.addLayout(col2_layout)
    root_layout.addLayout(col3_layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("jennyFunc")
    w.resize(640,480)  #窗口大小
    
    init_widget(w)

    w.show()
    sys.exit(app.exec_())
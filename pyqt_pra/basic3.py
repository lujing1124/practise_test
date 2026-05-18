from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QTextEdit, QPushButton
import sys

def click_func():
    print('sendding...')

def init_widget(w: QWidget):
    layout = QVBoxLayout()
    
    edit = QLineEdit()
    edit.setPlaceholderText("input username")
    edit.setText("abc")
    edit.setParent(w)
    layout.addWidget(edit)
    print("edit:",edit.text())
    
    edit_pwd = QLineEdit()
    edit_pwd.setParent(w)
    layout.addWidget(edit_pwd)
    w.setLayout(layout)
    
    text_edit = QTextEdit()
    text_edit.setPlainText("I'm ")
    layout.addWidget(text_edit)

    btn = QPushButton()
    btn.setText('send')
    btn.clicked.connect(click_func)
    layout.addWidget(btn)

    btn2 = QPushButton()
    btn2.setText('send2')
    btn2.clicked.connect(lambda:print("sendding234..."))
    layout.addWidget(btn2)

    btn3 = QPushButton()
    btn3.setText('send3')
    btn3.clicked.connect(QApplication.quit)
    layout.addWidget(btn3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("jennyFunc")
    w.resize(640,480)  #窗口大小
    
    init_widget(w)

    w.show()
    sys.exit(app.exec_())
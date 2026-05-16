from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QTextEdit
import sys

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("jennyFunc")
    w.resize(1280,960)  #窗口大小
    
    init_widget(w)

    w.show()
    sys.exit(app.exec_())
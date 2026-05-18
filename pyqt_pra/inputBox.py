from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtWidgets import QMessageBox, QInputDialog
import sys

def click_func():
    print('sendding...')

def dialog_info():
    # QMessageBox.information(w,"del info","Are you sure del?")
    text,con = QInputDialog.getText(
        w,"tip","input username:"
    )
    print(text,con)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("jennyFunc")
    w.resize(640,480)  #窗口大小
    
    root_layout = QVBoxLayout(w)
    btn = QPushButton("dialog")
    btn.clicked.connect(dialog_info)
    root_layout.addWidget(btn)

    w.show()
    sys.exit(app.exec_())
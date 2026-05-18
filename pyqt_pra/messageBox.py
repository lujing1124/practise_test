from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtWidgets import QMessageBox
import sys

def click_func():
    print('sendding...')

def del_user():
    # QMessageBox.information(w,"del info","Are you sure del?")
    result = QMessageBox.question(w,"tip","Are you sure del user?",
                        buttons=QMessageBox.Yes | QMessageBox.Cancel, defaultButton=QMessageBox.Cancel)
    if result == QMessageBox.Yes:
        print("del")
    else:
        print("no")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("jennyFunc")
    w.resize(640,480)  #窗口大小
    
    root_layout = QVBoxLayout(w)
    btn = QPushButton("del")
    btn.clicked.connect(del_user)
    root_layout.addWidget(btn)

    w.show()
    sys.exit(app.exec_())
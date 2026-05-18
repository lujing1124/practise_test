from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout, QTextEdit, QPushButton
import sys

def on_submit():
    print('username:',edit_user.text())
    print('password:',edit_psw.text())
    print('phoen:',edit_phone.text())

def init_widget(w: QWidget):
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("jennyFunc")
    w.resize(640,480)  #窗口大小
    
    # init_widget(w)
    layout = QFormLayout()
    w.setLayout(layout)

    edit_user = QLineEdit()
    edit_psw = QLineEdit()
    edit_psw.setEchoMode(QLineEdit.Password)
    edit_phone = QLineEdit()
    btn = QPushButton("send")
   
    btn.clicked.connect(on_submit)
    layout.addRow("username:",edit_user)
    layout.addRow("password:",edit_psw)
    layout.addRow("phone:",edit_phone)
    layout.addRow(btn)

    w.show()
    sys.exit(app.exec_())
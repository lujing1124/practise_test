from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtWidgets import QRadioButton,QButtonGroup,QCheckBox,QLabel,QPushButton
import sys

def btn_state(flag,text,arg):
    print(f"{flag}:{text}->{arg}")

def btn_update():
    print("aa",btn1.isChecked(),btn2.isChecked(),btn3.isChecked())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("jennyFunc")
    w.resize(640,480)  #窗口大小
    
    root_layout = QVBoxLayout(w)
    btn1 = QCheckBox("抽烟")
    btn2 = QCheckBox("气老婆")
    btn3 = QCheckBox("喝酒")

    btn1.stateChanged.connect(lambda arg:btn_state(1,"抽烟",arg))
    btn2.stateChanged.connect(lambda arg:btn_state(2,"气老婆",arg))
    btn3.stateChanged.connect(lambda arg:btn_state(3,"喝酒",arg))

    submit_btn = QPushButton()
    submit_btn.clicked.connect(btn_update)

    root_layout.addWidget(QLabel("男人的爱好："))
    root_layout.addWidget(btn1)
    root_layout.addWidget(btn2)
    root_layout.addWidget(btn3)
    root_layout.addWidget(submit_btn)


    w.show()
    sys.exit(app.exec_())
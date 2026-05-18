from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QRadioButton,QButtonGroup
import sys

def on_group_toggle(btn: QRadioButton):
    print(btn.text(), btn.isChecked())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("jennyFunc")
    w.resize(640,480)  #窗口大小
    
    root_layout = QVBoxLayout(w)
    btn1 = QRadioButton("男")
    btn2 = QRadioButton("女")
    btn1.setChecked(True) # 默认选中第一个
    # radio2.setChecked(True)

    group = QButtonGroup()
    group.addButton(btn1)
    group.addButton(btn2)
    group.buttonToggled.connect(on_group_toggle)

    root_layout.addWidget(btn1)
    root_layout.addWidget(btn2)

    w.show()
    sys.exit(app.exec_())
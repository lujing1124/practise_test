from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui.Ui_net_assist_widget import Ui_NetAssistWidget
import socket
import threading
import sys
from common import utils



class NetAssistWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.ui = Ui_NetAssistWidget()
        self.ui.setupUi(self)
        self.init_ui()

    def run_tcp_client(self,target_ip,target_port):
        tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            target_addr = (target_ip, int(target_port))
            tcp_client.connect(target_addr)
            print("2.服务器连接成功")
            sockname = tcp_client.getsockname()
            print("sockname",sockname)

            bytes_data = tcp_client.recv(2048)
            str_data = utils.decode_data(bytes_data)
            print('3.strData:',str_data)
        except Exception as e:
            print("exception:",e)
        finally:
            print("4.close")
            tcp_client.close()


    def on_connect_clicked(self):
        target_port = self.ui.edit_target_port.text()
        target_ip = self.ui.edit_target_ip.text()
        # mode = self.ui.cb_mode.text()
        print(f"1.connect {target_ip}:{target_port}")
        if target_ip == "" or target_port == "":
            print("请输入IP和端口")
            return

        thread = threading.Thread(
            target=self.run_tcp_client, 
            args=(target_ip,target_port),
            daemon=True
        )
        thread.start()
        
    def init_ui(self):
        self.ui.edit_target_ip.setText("127.0.0.1")
        self.ui.edit_target_port.setText("8888")
        self.ui.btn_connect.clicked.connect(self.on_connect_clicked)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = NetAssistWidget()

    w.show()
    sys.exit(app.exec_())
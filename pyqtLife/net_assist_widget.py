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
        self.tcp_client = None
        self.init_ui()

    def update_connect_status(self):
        if self.tcp_client is not None:
            self.ui.btn_connect.setText("断开连接（已连接）")
            icon = QIcon()
            icon.addPixmap(QPixmap(":/icon/connect"), QIcon.Normal, QIcon.Off)
            self.ui.btn_connect.setIcon(icon)
        else:
            self.ui.btn_connect.setText("连接网络")
            icon = QIcon()
            icon.addPixmap(QPixmap(":/icon/disc"), QIcon.Normal, QIcon.Off)
            self.ui.btn_connect.setIcon(icon)
    def run_tcp_client(self,target_ip,target_port):
        self.tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            target_addr = (target_ip, int(target_port))
            self.tcp_client.connect(target_addr)
            print("2.服务器连接成功")
            
            local_ip, local_port = self.tcp_client.getsockname()
            print("sockname",local_ip, local_port)
            self.ui.cb_local_ip.setCurrentIndex(self.ui.cb_local_ip.findText(local_ip))
            self.ui.edit_local_port.setText(str(local_port))
            self.update_connect_status()
            while True:
                bytes_data = self.tcp_client.recv(2048)
                if bytes_data:
                    str_data = utils.decode_data(bytes_data)
                    print('3.strData:',str_data)
                    self.ui.edit_recv.append(str_data)
                else:
                    break
        except Exception as e:
            print("exception:",e)
        finally:
            print("4.close")
            if self.tcp_client is not None:
                self.tcp_client.close()
                self.tcp_client = None
                self.update_connect_status()

    def on_send_clicked(self):
        if self.tcp_client is None:
            print("请先连接")
            return
        text = self.ui.edit_send.toPlainText()
        self.tcp_client.send(text.encode("utf8"))
        print(text)
    
    def handle_client_connect(self):
        if self.tcp_client is not None:
            print("已连接，断开")           
            self.tcp_client.close()
            self.tcp_client = None
            self.update_connect_status()
            return
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
    
    def handle_new_client(self):
        pass
    
    def run_tcp_server(self,server_ip,server_port):
        tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server.bind((server_ip,int(server_port)))
        tcp_server.listen(128)
        client_socket,client_addr = tcp_server.accept()
        client_socket.send(f"welcome {client_addr}".encode())
        while True:
            bytes_data = client_socket.recv(1024)
            if bytes_data:
                msg = utils.decode_data(bytes_data)
                self.ui.edit_recv.append(msg)
            else:
                client_socket.close()
                break
        
        
    def handle_server_run(self):
        print('开启服务器')
        server_ip = self.ui.edit_target_ip.text()
        server_port = self.ui.edit_target_port.text()
        if server_port == '':
            print('先输入端口')
            return
        # self.run_tcp_server(server_ip,server_port)
        thread = threading.Thread(
            target=self.run_tcp_server,
            args=(server_ip, server_port), daemon=True
        )    
        thread.start()
    
    def on_connect_clicked(self):
        current_mode = self.ui.cb_mode.currentIndex()
        if current_mode == 0:       
            self.handle_client_connect() 
        elif current_mode == 1:
            self.handle_server_run()
    def no_mode_changed(self):
        index = self.ui.cb_mode.currentIndex()    
        if index == 0:
            self.ui.lable_ip.setText("服务器IP：")
            self.ui.lable_port.setText("服务器port：")
        else:
            self.ui.lable_ip.setText("本地IP：")
            self.ui.lable_port.setText("本地port：")
    def init_ui(self):
        self.ui.edit_target_ip.setText("127.0.0.1")
        self.ui.edit_target_port.setText("8888")
        local_ips = utils.get_local_ip()
        self.ui.btn_connect.clicked.connect(self.on_connect_clicked)
        self.ui.btn_send.clicked.connect(self.on_send_clicked)
        self.ui.cb_local_ip.addItems(local_ips)
        self.ui.cb_mode.currentIndexChanged.connect(self.no_mode_changed)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = NetAssistWidget()

    w.show()
    sys.exit(app.exec_())
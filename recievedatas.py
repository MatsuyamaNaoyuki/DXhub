import socket
import struct
class Motioncapture():
    def __init__(self):


        # マルチキャストグループのIPアドレスとポート番号を設定
        self.MCAST_GRP = '239.239.239.52'
        self.MCAST_PORT = 5231

        # ソケットを作成
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

        # 受信バッファのサイズを設定
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # ソケットをバインド
        self.sock.bind(('', self.MCAST_PORT))

        # マルチキャストグループに参加
        self.mreq = struct.pack("4sl", socket.inet_aton(self.MCAST_GRP), socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, self.mreq)

    def get_data(self):
        data, addr = self.sock.recvfrom(1024)
        return data
    
    def change_data(self, data):
        byte_len = len(data)
        for i in range(28,byte_len - 40, 4):
            byte_chunk = data[i:i+4]
    
    # 4バイト未満の場合はスキップ
            if len(byte_chunk) < 4:
                continue
    
    # 4バイトをfloat型に変換
            float_value = struct.unpack('f', byte_chunk)[0]
            print(float_value,end=" ")
        

mc = Motioncapture()
data = mc.get_data()
mc.change_data(data)
byte_len = len(data)
    



import socket
import struct
import sys,os, time, datetime, csv
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class MotionCapture():
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

        self.datas = []



    def get_data(self):
        now_time  = datetime.datetime.now()
        data, addr = self.sock.recvfrom(1024)
        formatted_now = now_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        return data, formatted_now
    
    def store_data(self, data, now_time):
        byte_len = len(data)
        floatdatas = []
        for i in range(28,byte_len - 40, 4):
            byte_chunk = data[i:i+4]
            if len(byte_chunk) < 4:
                continue
            float_value = struct.unpack('f', byte_chunk)[0]
            floatdatas.append(float_value)
        floatdatas.insert(0, now_time)
        self.datas.append(floatdatas)

        

# mc = Motioncapture()
# data,nowtime = mc.get_data()
# mc.change_data(data, nowtime)
# data,nowtime = mc.get_data()
# mc.change_data(data, nowtime)
# print(mc.datas)
# filename = 'test'
# now = datetime.datetime.now()
# filename = os.path.dirname(__file__) +"\\" + filename + now.strftime('%Y%m%d_%H%M%S') + '.csv'

# with open(filename, 'w',newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(mc.datas)


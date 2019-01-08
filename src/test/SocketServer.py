import socket
from threading import Thread
import math


def handle(_conn, _addr):
    print(str(addr) + " has being connected with server.")
    while True:
        # 获取消息长度
        flag = _conn.recv(4)
        length = int.from_bytes(flag, byteorder='big')
        if length == 0:  # 客户端退出
            _conn.close()
            print(str(addr) + ' client quit.')
            break
        b_size = 3 * 1024  # 注意utf8编码中汉字占3字节，英文占1字节
        times = math.ceil(length / b_size)
        content = ''
        for i in range(times):
            seg_b = _conn.recv(b_size)
            content += str(seg_b, encoding='utf-8')
        print(str(addr) + ' content from client: ' + content)


if __name__ == "__main__":
    sk = socket.socket()
    sk.bind(('127.0.0.1', 12345))
    sk.listen(5)  # 最大挂起数5
    while True:
        conn, addr = sk.accept()
        Thread(target=handle, args=(conn, addr)).start()

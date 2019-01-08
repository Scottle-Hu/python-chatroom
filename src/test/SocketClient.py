import socket

if __name__ == "__main__":
    sk = socket.socket()
    sk.connect(('127.0.0.1', 12345))
    while True:
        content = input("input something, or 'q' to quit:\n")
        if content == 'q':
            sk.sendall(int(0).to_bytes(4, byteorder='big'))
            break
        # 先发送内容的长度
        sk.sendall(bytes(content, encoding='utf-8').__len__().to_bytes(4, byteorder='big'))
        # 再发送内容
        sk.sendall(bytes(content, encoding='utf-8'))
    sk.close()

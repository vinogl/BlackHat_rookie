import socket


address = ('192.168.1.101', 8080)

while True:
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect(address)

    # 发送消息
    message = str(input('local: '))
    tcp.send(message.encode('utf-8'))
    # 接受消息
    response = tcp.recv(1024)
    print('remote: %s' % response.decode('utf-8'))

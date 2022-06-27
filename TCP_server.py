import socket
import threading
import time


def get_host_ip():
    """获取本机ip地址"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(('8.8.8.8', 80))
        ip = sock.getsockname()[0]
    finally:
        sock.close()
    return ip


def handle_client(client):
    """客户处理线程的工作"""
    # 接受信息
    message = client.recv(1024)
    print('remote: %s' % message.decode('utf-8'))
    time.sleep(0.1)
    # 发送信息
    response = str(input('local: '))
    client.send(response.encode('utf-8'))


if __name__ == '__main__':
    print(get_host_ip())
    address = (get_host_ip(), 8080)

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    """
    setsockopt():
    SOL_SOCKET:对Socket层进行设置
    SO_REUSEADDR: 是否允许在bind过程中本地地址可重复使用(1: 允许)
    """
    tcp.bind(address)
    tcp.listen(5)

    while True:
        client, address = tcp.accept()
        # 添加一个线程，处理传入的数据
        handle_client_thread = threading.Thread(target=handle_client, args=(client,))
        handle_client_thread.start()

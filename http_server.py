import sys
import locale
import http.server
import socketserver
import socket


"""
此脚本通过http server共享文件：

1. 进入到共享文件地址 (切换文件后http_server.py要写绝对路径)

2. 运行 'python http_server.py <localhost> <port>'

3. url访问: http://<ip>:<port> (ip为localhost)
"""


def get_host_ip():
    """
    获取本机ip地址
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(('8.8.8.8', 80))
        ip = sock.getsockname()[0]
    finally:
        sock.close()
    return ip


localhost = get_host_ip()

ipv4 = len(sys.argv) < 2 and localhost or sys.argv[1]
port = len(sys.argv) < 3 and 8000 or locale.atoi(sys.argv[2])

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer((ipv4, port), handler)
print("HTTP server is at: http://%s:%d/" % (ipv4, port))
httpd.serve_forever()

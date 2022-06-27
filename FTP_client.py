import ftplib


class FTPClient:
    def __init__(self, host, port, user, password, bufsize=1024):
        self.ftp = ftplib.FTP()
        self.ftp.connect(host=host, port=port)
        self.ftp.login(user=user, passwd=password)
        self.bufsize = bufsize

    def download(self, remote_path, local_path):
        with open(local_path, 'wb') as fp:
            self.ftp.retrbinary('RETR  ' + remote_path, fp.write, self.bufsize)
            self.ftp.set_debuglevel(0)

    def upload(self, remote_path, local_path):
        with open(local_path, 'rb') as fp:
            self.ftp.storbinary('STOR  ' + remote_path, fp, self.bufsize)
            self.ftp.set_debuglevel(0)


if __name__ == '__main__':
    host, port = '192.168.1.107', 8080
    user, password = 'admin', '123456'
    ftp_client = FTPClient(host, port, user, password)
    ftp_client.download('test.jpg', r'C:\Users\GL\Desktop\test.jpg')

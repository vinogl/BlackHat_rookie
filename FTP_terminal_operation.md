# 终端的FTP操作

### `ftp`交互远程连接

```
~$ ftp
ftp> open <ip> <port>
user:
password:
User logged in
```

### 基本操作:

```
ftp> get file_name new_name          # 下载指定文件
ftp> mget file_name file_name        # 下载多个文件
ftp> put file_name new_name          # 上传指定文件
ftp> send file_name new_name         # 上传指定文件
ftp> rename file_name new_file_name  # 重命名FTP服务器上的文件
ftp> delete file_name                # 删除FTP服务器上的文件
```

```
ftp> dir           # 显示服务器目录和文件列表
ftp> ls            # 显示服务器简易的文件列表
ftp> cd            # 进入服务器指定的目录
ftp> pwd           # 查看FTP服务器上的当前工作目录
ftp> help[cmd]     # 显示FTP命令的帮助信息
```

```
ftp> type          # 查看当前的传输方式
ftp> ascii         # 设定传输方式为ASCII码方式
ftp> binary        # 设定传输方式为二进制方式
```

### `python`通过`http server`共享文件：

1. 进入到共享文件地址

2. 指定端口分享

	* 终端直接运行

	```
	~$ python -m http.server <port>  # python3
	~$ python -m SimpleHTTPServer <port>  # python2
	```

	* 运行`http_server.py`脚本

	```
	~$ python /http_server.py <localhost> <port>
	```

3. `url`访问: `http://<ip>:<port>`(`ip`为`localhost`)

# !/usr/bin/python3.8
# -*- coding=utf-8 -*-
# from http.server import HTTPServer, CGIHTTPRequestHandler
# port = 80
# httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
# print('Starting simple httpd on port: ' + str(httpd.server_port))
# httpd.serve_forever()

import time
import re
import os

cmd = 'netstat -tulnp'




while True:
    time.sleep(1)
    test_cmd = os.popen(cmd).read()
    print('等待一秒重新开始监控！')
    if re.search(r'[\S\s]+(tcp\s+0\s+0\s+0.0.0.0\:80)\s+', test_cmd):
        print('HTTP (TCP/80) 服务已经被打开')
        break



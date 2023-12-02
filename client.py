import socket
import threading

def receive_message(server_socket):
    while True:
        msg = server_socket.recv(1024).decode('utf-8')
        if msg == 'END':
            break
        print(f"服务器: {msg}")
    server_socket.close()

def client():
    client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    client_socket.connect(('::1', 12345))  # 服务器的 IPv6 地址和端口

    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    receive_thread.start()

    while True:
        msg = input()
        if msg == 'END':
            client_socket.send(msg.encode('utf-8'))
            break
        client_socket.send(msg.encode('utf-8'))

if __name__ == "__main__":
    client()

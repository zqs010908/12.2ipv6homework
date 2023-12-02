import socket
import threading

def handle_client(client_socket):
    while True:
        msg = client_socket.recv(1024).decode('utf-8')
        if msg == 'END':
            break
        print(f"客户端: {msg}")
    client_socket.close()

def server():
    server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    server_socket.bind(('::1', 12345))  # IPv6 地址和端口
    server_socket.listen(5)
    print("服务器启动，等待连接...")

    client_socket, address = server_socket.accept()
    print(f"来自 {address} 的连接")

    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()

    while True:
        msg = input()
        if msg == 'END':
            client_socket.send(msg.encode('utf-8'))
            break
        client_socket.send(msg.encode('utf-8'))

    server_socket.close()

if __name__ == "__main__":
    server()
    

# Server side
import socket


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('172.17.30.81', 4000))
    print(socket.gethostname())
    server_socket.listen(1)
    client_socket, address = server_socket.accept()
    arr = []
    while(True):
        data = client_socket.recv(1024)

        if(data.decode('utf-8') == ''):
            client_socket.close()
        data = eval(data)
        arr.append(data)
        print("data: ",data)
        print("decoded: ", data)

    client_socket.close()
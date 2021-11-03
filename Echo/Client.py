import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = int(input('Введите здесь номер порта (default is 2000)\n'))
host = input('Введите здесь имя хоста (default is localhost)\n')
try:
    client.connect((host, port))
except (ConnectionRefusedError, socket.gaierror):
    print("Соединение сейчас недоступно.\nХотите установить значения по умолчанию? Y\\N")
    if input() == "Y":
        client.connect(('127.0.0.1', 2000))
    else:
        print('Попробуйте снова')
        exit()
print(client.recv(2048).decode('utf-8'))
try:
        while True:
            client.send(input('Введите текст для сервера:\n').encode('utf-8'))
            data = client.recv(2048).decode('utf-8')
            time.sleep(3)

            if data.lower() == 'exit':
                print('>>>\nДо свидания!\n<<<')
                client.send(encode('utf-8')
                client.shutdown(socket.SHUT_WR)
                exit()

            if data:
                print('\nData from server:')
                print(data, end='\n\n')
except KeyboardInterrupt:
    client.shutdown(socket.SHUT_WR)

import socket


"Открываем порт на прослушивание"
server = socket.create_server(("127.0.0.1", 8000))
"Настройка для освобождения порта после завершения работы скрипта"
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

"Устанавливаем лимит очереди на прослушивание"
server.listen(10)
try:
    while True:
        "Прием сетевых запросов"
        "Распаковка tuple в две переменные"
        client_socket, addres = server.accept()
        "Читаем и декодируем данные из client_socket"
        received_data = client_socket.recv(1024).decode("utf-8")

        print("Получили данные по сокету", received_data)
        "Получаем указазный путь после корня"
        path = received_data.split(" ")[1]
        response = f"HTTP/1.1 200 OK \nContent-Type: text/html; charset=utf-8\n\n" \
                    f"Введенный путь:<br />Path: {path}"
        "Отправляем ответ"
        client_socket.send(response.encode("utf-8"))
        "Прибиваем сокет"
        client_socket.shutdown(socket.SHUT_RDWR)
        "Прибиваем сервер"
except KeyboardInterrupt:
    server.shutdown(socket.SHUT_RDWR)
    server.close()
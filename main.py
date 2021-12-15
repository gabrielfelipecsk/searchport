import socket


def read_txt(path: str) -> str:
    with open(path, 'r') as file:
        return file.read().splitlines()


connection: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

location: str = '20.124.80.187'
current_port: int = 80


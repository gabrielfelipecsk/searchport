import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


class PortScan:
    
    status: bool = False

    host: str = ''

    port: int = 0

    def __init__(self, host: str, port: int) -> None:

        self.host: str = host
        self.port: int = port

        self.scan()

    def __repr__(self) -> str:
        return f'Host: {self.host} | Port: {self.port} | Status: {self.status}'

    def scan(self) -> None:
        try:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            response: int = s.connect_ex((self.host, self.port))

            self.status = True if response == 0 else False

        except Exception as Error:
            print(Error)
            self.status = False
        finally:
            s.close()


def scan_opened_in_range(host: str, init_range: int, final_range: int, max_workers: int = 20) -> list:
    futures: list = []
    data: list = []

    with ThreadPoolExecutor(max_workers=max_workers) as texecutor:

        for port in range(init_range, final_range + 1):
            futures.append(texecutor.submit(PortScan, host=host, port=port))

        for future in as_completed(futures):
            data.append(future.result())
        
        return data


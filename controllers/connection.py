import socket
import threading

def port_scan(host: str, port: int, scan_list: list):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        scan_list.append({'port': port, 'status': 'open'})
        s.close()
    except:
        scan_list.append({'port': port, 'status': 'close'})

def scan_opened_in_range(host: str, init_range: int, final_range: int, scan_list: list) -> list:
    print('Inicializing Scans...')

    for port in range(init_range, final_range + 1):
        print(f'Init Port -> {port}')
        t = threading.Thread(target=port_scan, args=(host, port, scan_list))
        t.start()
        print(port)

    print('Finish Scans!')


scan_list: list = []

scan_opened_in_range('20.124.80.187', 0, 100, scan_list)    
    
for sl in scan_list:
    print(sl)

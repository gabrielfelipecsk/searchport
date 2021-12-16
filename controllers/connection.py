import socket
import threading

def port_scan(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print("Port %d is open" % port)
        s.close()
    except:
        print("Port %d is closed" % port)


for port in range(1, 10000):
    print(f'Init Port -> {port}')
    t = threading.Thread(target=port_scan, args=('20.124.80.187', port))
    t.start()
    
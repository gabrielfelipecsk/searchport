import socket


def port_scan(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print("Port %d is open" % port)
        s.close()
    except:

        print("Port %d is closed" % port)

port_scan('20.124.80.187', 80)


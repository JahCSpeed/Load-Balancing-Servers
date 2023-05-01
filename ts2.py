import sys
import socket as mainSoc
FILE_PATH = "DNSTS2.txt"

def check_args(size, expectedSize):
    if size is not expectedSize:
        raise TypeError("Needed %d args" %(expectedSize))
        exit()

def populate_dns():
    file = open(FILE_PATH,"r")
    dns = {}
    for inputs in file:
        query = inputs.strip().split(" ")
        dns[query[0].lower()] = " ".join(query)
    file.close()
    return dns

def create_socket(bind):
    try:
        socket = mainSoc.socket(mainSoc.AF_INET,mainSoc.SOCK_STREAM)
        socket.bind(bind)
        socket.listen(5)
        print("[DNS TS2]: TS2 socket created")
    except:
        print("[DNS TS2]: ERROR OCCURED")
    return socket
def running(client_socket,dns):
    while True:
        data = client_socket.recv(2048).decode("utf-8").strip()
        print("[DNS TS2]: Received Message: " + str(data))
        if not data:
            return
        if data.lower() in dns:
            print("[DNS TS2]: Data found in DNS")
            return_data = dns.get(data.lower()) + ' IN'
            client_socket.send(return_data.encode("utf-8"))
def ts():
    check_args(len(sys.argv),2)
    dns = populate_dns()
    socket = create_socket(("", int(sys.argv[1])))
    host_name = mainSoc.gethostname()
    ip_addy = mainSoc.gethostbyname(host_name)
    print("[DNS TS1]: Running on Hostname, IP: " + host_name + ", " + ip_addy)
    client_socket = socket.accept()
    print("[DNS TS1]: Got a connection request from: " + str(client_socket[1]))
    running(client_socket[0],dns)
    client_socket[0].close()
    socket.close()
    exit()
    
ts()
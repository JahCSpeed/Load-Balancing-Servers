import sys
import socket as mainSoc

def check_args(size, expectedSize):
    if size is not expectedSize:
        raise TypeError("Needed %d args" %(expectedSize))
        exit()
    
def create_socket(bind,type):
    try:
        socket = mainSoc.socket(mainSoc.AF_INET,mainSoc.SOCK_STREAM)
        if type == 0:
            socket.bind(bind)
            socket.listen(5)
        elif type == 1:
            socket.connect(bind)
            socket.settimeout(5)
        print("[LS]: Socket created")
    except:
        print("[LS]: ERROR OCCURED")
    return socket
def running(client_socket,t1_socket,t2_socket):
    while True:
        data = client_socket.recv(2048).decode("utf-8").strip()
        if not data:
            return
        print("[LS]: Received from Client: " + data)
        t1_socket.send(data.encode("utf-8"))
        t2_socket.send(data.encode("utf-8"))
        try:
            ts1_data = t1_socket.recv(2048).decode("utf-8")
            print("[LS]: Data from [DNS TS1]: " + ts1_data)
            client_socket.send(ts1_data.encode('utf-8'))
        except mainSoc.timeout:
            print("[LS]: [DNS TS1] Timed Out")
            try:
                ts2_data = t2_socket.recv(4096).decode("utf-8")
                print("[LS]: Data from [TS2]: " + ts2_data)
                client_socket.send(ts2_data.encode("utf-8"))
            except mainSoc.timeout:
                print("[LS]: [DNS TS2] Timed Out")
                err_str = data + " - TIMED OUT"
                client_socket.send(err_str.encode("utf-8"))
def ls():
    check_args(len(sys.argv), 6)
    ls_socket = create_socket(("", int(sys.argv[1])),0)
    ts1_socket = create_socket((str(sys.argv[2]),int(sys.argv[3])),1)
    ts2_socket = create_socket((str(sys.argv[4]),int(sys.argv[5])),1)
    client_socket = ls_socket.accept()
    print('[LS]: Got a connection request from: ' + str(client_socket[1]))
    running(client_socket[0],ts1_socket,ts2_socket)
    ls_socket.close()
    ts1_socket.close() 
    ts2_socket.close()
ls()
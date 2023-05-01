import sys
import socket as mainSoc
QUERIE_PATH = "HOSTS.txt"
OUTPUT_PATH = "RESOLVED.txt"

def check_args(size, expectedSize):
    if size is not expectedSize:
        raise TypeError("Needed %d args" %(expectedSize))
        exit()
def get_queries():
	file = open(QUERIE_PATH, "r")
	queries = file.read().splitlines()
	file.close()	
	return queries

def create_socket(bind):
    try:
        socket = mainSoc.socket(mainSoc.AF_INET, mainSoc.SOCK_STREAM)
        socket.connect(bind)
        print ("[C]: Client socket created")
    except:
        print("[C]: ERROR OCCURED")
    return socket

def client():
    check_args(len(sys.argv), 3)
    queries = get_queries()
    client_socket = create_socket((str(sys.argv[1]), int(sys.argv[2])))
    file = open(OUTPUT_PATH,"w+")
    for entry in queries:
        print("[C]: Sent: " + entry)
        client_socket.send(entry.encode("utf-8"))
        message = client_socket.recv(2048).decode("utf-8")
        print ("[C]: The received response is: " + message)
        file.write(message + "\n")
    file.close()
    client_socket.close()

client()

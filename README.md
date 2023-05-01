# Load-Balancing-Servers
To run the LBS run the following commands in separate terminals. 
python ts1.py <ts1ListenPort> 
python ts2.py <ts2ListenPort> 
python ls.py <lsListenPort> <ts1Hostname> <ts1ListenPort> <ts2Hostname><ts2ListenPort> 
python client.py <lsHostname> <lsListenPort>

• ts1ListenPort and ts2ListenPort are ports accepting incoming connections at TS1 and TS2 (resp.) from LS;
• lsListenPort is the port accepting incoming connections from the client at LS;
• lsHostname, ts1Hostname, and ts2Hostname are the hostnames of the machines running LS, TS1, and TS2 (resp.)

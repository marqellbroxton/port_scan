import socket
import sys
from datetime import datetime

# Input of Domain address
Server = input("Enter a Domain Address to scan: ")
ServerIP = socket.gethostbyname(Server)

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", ServerIP)
print("-" * 60)

# Check what time the scan started
time1 = datetime.now()

# Scan of ports in range of 1 - 1000. Can be adjusted to however many ports you want to scan
try:
    for port in range(1, 1000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        scan = sock.connect_ex((ServerIP, port))
        if scan == 0:
            print("Port {}: 	 Open".format(port))
#        else:
#           print("Port {}: 	 Closed".format(port))
#       sock.close()

# If a user escapes while ports are being scanned
except KeyboardInterrupt:
    print("Scan was canceled by user.")
    sys.exit()

# Error entering an invalid domain address
except socket.gaierror:
    print('Hostname Invalid.')
    sys.exit()

# Error for not being able to connect to server
except socket.error:
    print("Unable to reach server")
    sys.exit()

# Checking time again
time2 = datetime.now()

# Calculation of how long it took to scan
totalTime = time2 - time1

# Displaying how long the scan took
print('Scan was completed in: ', totalTime)


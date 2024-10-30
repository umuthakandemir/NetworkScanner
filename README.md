#Network Scanner
This project provides a simple network scanner application using Python and the scapy library. It scans the network for devices based on a given IP range entered through the command line and lists the IP and MAC addresses of active devices.

##Features
Network scanning: Scans the network for devices using ARP requests in the specified IP range.
Easy to use: Quickly perform a scan by entering the IP range via the command line.
Requirements
Python 3.x
Scapy library
To install the Scapy library:

 ```bash
pip install scapy
```

Usage
You can run the script from the terminal or command line as follows:

```bash
python network_scanner.py -r <IP_RANGE>
```

##Example:

```bash
python network_scanner.py -r 192.168.1.0/24
```

This command will scan for all devices in the 192.168.1.0/24 IP range.

##Output
Upon completion of the scan, it will display the IP and MAC addresses of all detected devices.

##Code Explanation
getSourceInfo: Used to get the IP range from the command line.
requestFunction: Combines ARP and Ethernet packets to scan a specified IP range.
run: Initiates the scanning process, obtains the IP range from the user, starts the scan, and displays the results.
# **Legal Disclaimer**
>This software is intended for educational and testing purposes only. Unauthorized or illegal network scanning can be punishable by law. We do not accept any responsibility for any legal consequences that may arise from the unauthorized use of this tool. It is the user's responsibility to use the tool within legal boundaries.

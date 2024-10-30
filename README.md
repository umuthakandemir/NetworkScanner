# Network Scanner
This project provides a simple network scanner application using Python and the scapy library. It scans the network for devices based on a given IP range entered through the command line and lists the IP and MAC addresses of active devices.

## Features
Network scanning: Scans the network for devices using ARP requests in the specified IP range.
Easy to use: Quickly perform a scan by entering the IP range via the command line.
Requirements
Python 3.x
Scapy library
To install the Scapy library:

 ```bash
pip install scapy
```

## Usage
You can run the script from the terminal or command line as follows:

```bash
python network_scanner.py -r <IP_RANGE>
```

## Example:

```bash
python network_scanner.py -r 192.168.1.0/24
```

This command will scan for all devices in the 192.168.1.0/24 IP range.

## Output
Upon completion of the scan, it will display the IP and MAC addresses of all detected devices.

## **LıKE:**
```bash
python scan.py -r 10.0.2.0/24                                                  
Scanning Network. Please wait..
Begin emission:
Finished sending 256 packets.
***
Received 3 packets, got 3 answers, remaining 253 packets
Ether / ARP who has 10.0.2.1 says 10.0.2.4 ==> Ether / ARP is at 52:54:00:12:35:00 says 10.0.2.1 / Padding
Ether / ARP who has 10.0.2.2 says 10.0.2.4 ==> Ether / ARP is at 52:54:00:12:35:00 says 10.0.2.2 / Padding
Ether / ARP who has 10.0.2.3 says 10.0.2.4 ==> Ether / ARP is at 08:00:27:f7:fc:e4 says 10.0.2.3 / Padding
```

## Code Explanation
getSourceInfo: Used to get the IP range from the command line.
requestFunction: Combines ARP and Ethernet packets to scan a specified IP range.
run: Initiates the scanning process, obtains the IP range from the user, starts the scan, and displays the results.
# **Legal Disclaimer**
>This software is intended for educational and testing purposes only. Unauthorized or illegal network scanning can be punishable by law. We do not accept any responsibility for any legal consequences that may arise from the unauthorized use of this tool. It is the user's responsibility to use the tool within legal boundaries.

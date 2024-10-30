import scapy.all as scapy
import optparse as parse

defaultMac = "ff:ff:ff:ff:ff:ff"
def getSourceInfo():
    parseOption = parse.OptionParser()
    parseOption.add_option("-r","--range",dest="ipRange",help="Needed for network scan")
    (userInput,argument) = parseOption.parse_args()
    return userInput.ipRange
def requestFunction(ip):
    arpRequestPackage = scapy.ARP(pdst=ip)
    brodcastDestinationPackage = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combinedPackage = brodcastDestinationPackage/arpRequestPackage
    return scapy.srp(combinedPackage,timeout=1)
def run():
    print("Scanning Network. Please wait..")
    ipRange = getSourceInfo()
    if not ipRange:
        print("Sorry. Not scanned Network. Please enter ip range. like:10.0.2.0/24")
    else:
        (answerList,unanswerList) = requestFunction(ipRange)
        answerList.summary()
run()
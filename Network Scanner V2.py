import scapy.all as scapy

# just using arping

print("Use the scan function now")


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether()   # Creates an ethernet frame
    scapy.ls(scapy.Ether())


scan("192.168.0.1")

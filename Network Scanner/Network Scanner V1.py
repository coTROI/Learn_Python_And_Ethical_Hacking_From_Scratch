import scapy.all as scapy

# just using arping


def scan(ip):
    scapy.arping(ip)


scan("192.168.0.1/24")

import scapy.all as scapy

# just using arping

print("Use the scan function now")


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Creates an ethernet frame
    # scapy.ls(scapy.Ether())    # Know details on the ethernet frame
    broadcast.show()
    arp_request_broadcast = broadcast / arp_request  # Creating two new packets and combinig them to produce the required output
    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()


scan("10.0.2.2")

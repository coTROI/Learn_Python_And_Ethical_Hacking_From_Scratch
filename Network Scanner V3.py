import scapy.all as scapy

# just using arping


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Creates an ethernet frame
    arp_request_broadcast = broadcast / arp_request  # Creating two new packets and combinig them to produce the required output
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP \t\t\t\tMac Address\n--------------------------")

    for element in answered_list:
        print(element[1].psrc+"\t\t"+element[1].hwsrc)
        print()
        print("------------------------")


scan("10.0.2.1/24")

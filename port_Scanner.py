from scapy.all import sniff, tcpdump

# Dictionary to track scanned ports
ports_dict = {}


# Packet processing function
def detect_port_scan(packet):
    if packet.haslayer(tcpdump):
        src_ip = packet[0][1].src
        dst_port = packet[tcpdump].dport

        # Update port scans record
        if src_ip not in ports_dict:
            ports_dict[src_ip] = set()
        ports_dict[src_ip].add(dst_port)

        # If more than 10 ports have been scanned by the same IP, raise an alert
        if len(ports_dict[src_ip]) > 10:
            print(f"[ALERT] Potential port scan detected from {src_ip}!")


# Sniff on the interface
sniff(iface="en0", filter="tcp", prn=detect_port_scan, store=0)

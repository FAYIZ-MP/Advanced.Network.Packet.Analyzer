from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "Unknown"
        
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        
        print(f"[+] Packet Captured: {protocol} | Source: {src_ip} -> Destination: {dst_ip}")
        
        if Raw in packet and packet[Raw].load:
            print(f"Payload: {packet[Raw].load[:100].decode(errors='ignore')}...")
            print("-" * 50)

if __name__ == "__main__":
    # Replace this with the correct NPF interface
    interface = "\\Device\\NPF_{8280114B-FD8C-4C85-B68E-C068F262EB64}"  

    print(f"Starting Packet Sniffer on {interface}... Press Ctrl+C to stop.")
    sniff(prn=packet_callback, store=False, iface=interface)

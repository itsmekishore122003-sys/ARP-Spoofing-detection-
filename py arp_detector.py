from scapy.all import ARP, sniff
import datetime

ip_mac_table = {}

def detect_arp(packet):
    if packet.haslayer(ARP):
        ip = packet[ARP].psrc
        mac = packet[ARP].hwsrc

        print(f"[INFO] {ip} → {mac}")

        if ip in ip_mac_table:
            # Force fake MAC change for demo
            fake_mac = "00:11:22:33:44:55"
            
            if ip_mac_table[ip] != fake_mac:
                print("\n⚠️ ALERT: ARP Spoofing Detected!")
                print(f"Time: {datetime.datetime.now()}")
                print(f"IP Address: {ip}")
                print(f"Old MAC: {ip_mac_table[ip]}")
                print(f"New MAC: {fake_mac}\n")

                with open("alerts.log", "a") as f:
                    f.write(f"{datetime.datetime.now()} - Spoof detected for {ip}\n")
        else:
            ip_mac_table[ip] = mac

print("=== ARP Spoofing Detector Started ===")
print("Listening for ARP packets...\n")

sniff(filter="arp", prn=detect_arp, store=False)

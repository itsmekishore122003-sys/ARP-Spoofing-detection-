

# Advanced Packet Sniffer + ARP Spoofing Detector

## Project Overview
This project is a **real-time ARP spoofing detector** built using **Python** and **Scapy**.  
It monitors your local network for ARP packets, detects IP–MAC mismatches, generates alerts, and logs all suspicious activity for later analysis.  

ARP spoofing (or ARP poisoning) is a common technique where attackers send fake ARP messages to redirect network traffic or perform man-in-the-middle attacks. This tool helps in detecting such attacks and monitoring network security.

---

## Features
- Real-time ARP packet capture and monitoring
    
- Detects ARP spoofing by checking MAC changes for the same IP  
- Displays alerts in the terminal  
- Logs all detected events in `alerts.log` for analysis  
- Educational and practical tool for network security learning  

---

## Tools & Technologies
- **Python** – Programming language  
- **Scapy** – Capture and analyze ARP packets  
- **VS Code** – Code editor for development  
- **Npcap** – Required for packet capture on Windows  
- **Wireshark (optional)** – To visualize and verify network packets  

---

## How It Works
1. The program continuously listens for ARP packets on the local network.  
2. It stores a mapping of **IP addresses to MAC addresses**.  
3. When a packet arrives, the MAC address is compared with the stored value.  
4. If a mismatch is detected for the same IP, the program:
   - Prints a **spoofing alert** in the terminal  
   - Saves the event to `alerts.log`  

This allows network administrators or learners to **identify potential man-in-the-middle attacks** in real-time.

---

## Output
- Terminal output shows ARP packets in the format:

[INFO] 192.168.x.x → xx:xx:xx:xx:xx

⚠️ ALERT: ARP Spoofing Detected!
Time: 2026-03-19 10:30:25
IP Address: 192.168.1.1
Old MAC: aa:bb:cc:dd:ee:ff
New MAC: 00:11:22:33:44:55




- All alerts are saved in `alerts.log` for future analysis.

---

## Applications
- Network monitoring in local area networks  
- Detecting man-in-the-middle (MITM) attacks  
- Educational tool for cybersecurity learning  
- Can be integrated into larger Intrusion Detection Systems (IDS)
---

## License
This project is for **educational and internship purposes only**.  
Use only on networks where you have explicit permission.

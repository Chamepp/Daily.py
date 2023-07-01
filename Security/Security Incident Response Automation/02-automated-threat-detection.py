import time
import socket
import pyshark

# Network interface to monitor
interface = 'eth0'

# Set up a capture filter to focus on relevant traffic
capture_filter = 'not arp and not icmp'

# Function to analyze captured packets
def analyze_packet(packet):
    # Extract relevant information from the packet
    src_ip = packet.ip.src
    dst_ip = packet.ip.dst
    protocol = packet.transport_layer
    src_port = packet[packet.transport_layer].srcport
    dst_port = packet[packet.transport_layer].dstport

    # Perform your custom analysis logic here
    # Example: Check for suspicious patterns or potential threats
    if 'malware' in packet or 'attack' in packet:
        print(f'Suspicious packet detected from {src_ip} to {dst_ip} - Protocol: {protocol}, Source Port: {src_port}, Destination Port: {dst_port}')

# Set up the packet capture
capture = pyshark.LiveCapture(interface=interface, display_filter=capture_filter)

# Start capturing packets indefinitely
try:
    print(f"Starting network traffic monitoring on {interface}...")
    print("Analyzing packets (Ctrl+C to stop)...\n")
    for packet in capture.sniff_continuously():
        analyze_packet(packet)
except KeyboardInterrupt:
    print("\nNetwork traffic monitoring stopped.")

# Close the capture when done
capture.close()


import pyshark

def analyze_network_traffic(interface, packet_count):
    capture = pyshark.LiveCapture(interface=interface, only_summaries=True, display_filter='tcp')

    print(f"Capturing network traffic on interface {interface}...")

    # Start capturing packets
    capture.sniff(packet_count)

    print("Analysis Results:")
    print("-----------------")

    # Iterate over captured packets and analyze each one
    for packet in capture:
        source_ip = packet.source
        destination_ip = packet.destination
        protocol = packet.protocol
        length = packet.length
        timestamp = packet.sniff_time.strftime("%Y-%m-%d %H:%M:%S")

        print(f"Timestamp: {timestamp}")
        print(f"Source IP: {source_ip}")
        print(f"Destination IP: {destination_ip}")
        print(f"Protocol: {protocol}")
        print(f"Packet Length: {length}")
        print("-----------------")

    capture.close()

# Example usage
interface = 'eth0'  # Update with your network interface name
packet_count = 10  # Number of packets to capture and analyze

analyze_network_traffic(interface, packet_count)


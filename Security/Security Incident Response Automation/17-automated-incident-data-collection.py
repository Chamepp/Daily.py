import pyshark

def analyze_network_traffic(interface):
    capture = pyshark.LiveCapture(interface=interface)
    capture.sniff(timeout=10)  # Capture network traffic for 10 seconds

    # Process captured packets
    for packet in capture:
        # Extract relevant information from the packet
        source_ip = packet.ip.src
        destination_ip = packet.ip.dst
        protocol = packet.transport_layer
        length = packet.length
        timestamp = packet.sniff_time

        # Perform analysis or further processing on the captured packet
        # Example: Print relevant information about each packet
        print(f"Source IP: {source_ip} | Destination IP: {destination_ip} | Protocol: {protocol} | Length: {length} | Timestamp: {timestamp}")

    capture.close()

# Example usage
interface_name = "eth0"  # Replace with your network interface name
analyze_network_traffic(interface_name)


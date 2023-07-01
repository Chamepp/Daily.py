import pyshark

# Capture network traffic
capture = pyshark.LiveCapture(interface='eth0')

# Define a display filter to focus on specific traffic of interest
display_filter = 'http'

# Analyze network packets
for packet in capture.sniff_continuously(packet_count=10):
    if display_filter in packet:
        print(packet)


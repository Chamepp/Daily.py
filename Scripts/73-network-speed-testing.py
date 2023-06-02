import speedtest

def measure_network_speed():
    # Create a Speedtest object
    st = speedtest.Speedtest()

    print("Testing network speed...")
    
    # Perform the speed test
    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6  # Convert to Mbps

    # Print the results
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

# Call the function to measure network speed
measure_network_speed()

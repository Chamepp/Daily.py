import datetime
import time
import os
import sys

# Function to check and notify about events
def check_events(events_file):
    # Load events from file
    events = []
    with open(events_file, 'r') as file:
        for line in file:
            event = line.strip()
            events.append(event)

    # Get current date and time
    current_datetime = datetime.datetime.now()

    # Check if any events are due
    for event in events:
        event_datetime = datetime.datetime.strptime(event, '%Y-%m-%d %H:%M:%S')

        if current_datetime >= event_datetime:
            print("Event reminder:", event)

    # Wait for a while before checking again
    time.sleep(60)  # Check every minute

# Main function
def main():
    # Check if events file exists
    events_file = "events.txt"
    if not os.path.isfile(events_file):
        print("No events file found. Please create 'events.txt' and add events in the format 'YYYY-MM-DD HH:MM:SS'.")
        sys.exit(1)

    # Continuously check for events
    while True:
        check_events(events_file)

# Run the script
if __name__ == '__main__':
    main()

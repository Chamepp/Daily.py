from twilio.rest import Client

# Your Twilio account SID and authentication token
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Function to send an SMS
def send_sms(to_number, message):
    try:
        # Send the SMS
        message = client.messages.create(
            body=message,
            from_="YOUR_TWILIO_PHONE_NUMBER",
            to=to_number
        )
        print(f"SMS sent to {to_number} successfully.")
    except Exception as e:
        print(f"Failed to send SMS: {str(e)}")

# Function to receive an SMS
def receive_sms():
    try:
        # Retrieve the last received SMS
        message = client.messages.list(limit=1)[0]
        sender_number = message.from_
        sms_body = message.body
        print(f"Received SMS from {sender_number}: {sms_body}")
    except Exception as e:
        print(f"Failed to receive SMS: {str(e)}")

# Example usage
send_sms("+1234567890", "Hello from Python!")
receive_sms()

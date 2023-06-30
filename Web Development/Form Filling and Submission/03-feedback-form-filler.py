import requests

def submit_feedback(url, form_data):
    response = requests.post(url, data=form_data)
    
    if response.status_code == 200:
        print("Feedback submitted successfully!")
    else:
        print("Failed to submit feedback. Status code:", response.status_code)

# Example usage
feedback_url = "https://www.example.com/feedback"
feedback_data = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "feedback": "I love your website! It's user-friendly and informative."
}

submit_feedback(feedback_url, feedback_data)


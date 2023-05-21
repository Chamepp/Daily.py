import schedule
import time

def task():
    print("Task executed!")

def reminder():
    print("Don't forget to complete your task!")

# Schedule a task to run every day at 10:00 AM
schedule.every().day.at("10:00").do(task)

# Schedule a reminder to run every hour
schedule.every().hour.do(reminder)

# Main loop to continuously check and execute scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)

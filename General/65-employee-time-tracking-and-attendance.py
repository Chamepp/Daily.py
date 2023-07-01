import datetime

def track_employee_attendance():
    employee_name = input("Enter employee name: ")
    
    # Get the current date and time
    current_datetime = datetime.datetime.now()
    
    # Format the date and time
    date = current_datetime.date()
    time = current_datetime.time()
    
    # Print the attendance record
    print(f"{employee_name} checked in on {date} at {time}")
    
    # Save the attendance record to a file
    with open("attendance.txt", "a") as file:
        file.write(f"{employee_name},{date},{time}\n")

# Call the function to track employee attendance
track_employee_attendance()

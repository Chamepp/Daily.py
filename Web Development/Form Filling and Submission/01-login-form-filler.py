from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Website URL
url = "https://www.example.com/login"

# User credentials
username = "your_username"
password = "your_password"

# Initialize the WebDriver (adjust the path to your driver executable if necessary)
driver = webdriver.Chrome("path_to_chromedriver")

# Open the website
driver.get(url)

# Find the username and password input fields and fill them
username_field = driver.find_element_by_id("username")
username_field.send_keys(username)

password_field = driver.find_element_by_id("password")
password_field.send_keys(password)

# Submit the form by pressing the Enter key
password_field.send_keys(Keys.RETURN)

# Wait for the page to load (adjust the sleep time if necessary)
time.sleep(3)

# Perform any additional actions after successful login
# For example, you can navigate to a specific page or perform other tasks

# Close the browser
driver.quit()


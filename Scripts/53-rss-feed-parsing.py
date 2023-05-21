from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the Selenium driver
driver = webdriver.Chrome()  # Replace with the path to your Chrome driver executable

# Open the webpage
driver.get("https://example.com")  # Replace with the URL of the webpage with the form

# Find the form fields and fill them out
first_name = driver.find_element_by_id("first_name")  # Replace with the ID or selector of the first name field
first_name.send_keys("John")  # Replace with the desired first name

last_name = driver.find_element_by_id("last_name")  # Replace with the ID or selector of the last name field
last_name.send_keys("Doe")  # Replace with the desired last name

email = driver.find_element_by_id("email")  # Replace with the ID or selector of the email field
email.send_keys("john.doe@example.com")  # Replace with the desired email

# Submit the form
submit_button = driver.find_element_by_id("submit_button")  # Replace with the ID or selector of the submit button
submit_button.click()

# Close the browser
driver.quit()

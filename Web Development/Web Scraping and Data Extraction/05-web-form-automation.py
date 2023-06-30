from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Configure the Selenium WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate driver for your browser (e.g., Firefox, Safari)

# Open the target web page with the form
driver.get("https://www.example.com/form")

# Find and fill the form fields
name_field = driver.find_element_by_name("name")
name_field.send_keys("John Doe")

email_field = driver.find_element_by_name("email")
email_field.send_keys("johndoe@example.com")

message_field = driver.find_element_by_name("message")
message_field.send_keys("Hello, this is my message!")

# Submit the form
submit_button = driver.find_element_by_css_selector("input[type='submit']")
submit_button.click()

# Wait for the form submission to complete
driver.implicitly_wait(10)  # Adjust the wait time as needed

# Close the browser
driver.quit()


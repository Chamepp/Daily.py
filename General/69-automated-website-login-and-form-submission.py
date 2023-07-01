from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set the path to the chromedriver executable
chromedriver_path = "path/to/chromedriver"

# Create a new Chrome browser instance
driver = webdriver.Chrome(chromedriver_path)

# Open the website login page
driver.get("https://example.com/login")

# Find the username and password input fields and enter your credentials
username_field = driver.find_element_by_id("username-input")
username_field.send_keys("your_username")
password_field = driver.find_element_by_id("password-input")
password_field.send_keys("your_password")

# Submit the login form
password_field.send_keys(Keys.ENTER)

# Wait for the login process to complete (you may need to adjust the sleep time depending on the website)
driver.implicitly_wait(5)

# Find the form input fields and enter your data
input_field1 = driver.find_element_by_id("input-field1")
input_field1.send_keys("Data 1")
input_field2 = driver.find_element_by_id("input-field2")
input_field2.send_keys("Data 2")

# Submit the form
submit_button = driver.find_element_by_id("submit-button")
submit_button.click()

# Wait for the form submission to complete
driver.implicitly_wait(5)

# Close the browser
driver.quit()

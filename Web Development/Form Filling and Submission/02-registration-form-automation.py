from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # You may need to specify the path to the Chrome driver executable

# Open the registration form URL
driver.get("https://example.com/registration-form")

# Find the input fields and submit button
username_field = driver.find_element_by_id("username")
email_field = driver.find_element_by_id("email")
password_field = driver.find_element_by_id("password")
submit_button = driver.find_element_by_id("submit")

# Provide the registration details
username_field.send_keys("JohnDoe")
email_field.send_keys("johndoe@example.com")
password_field.send_keys("password123")

# Submit the registration form
submit_button.click()

# Wait for the page to load (optional)
driver.implicitly_wait(5)

# Close the browser
driver.quit()


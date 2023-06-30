from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (you'll need to download the appropriate browser driver)
driver = webdriver.Chrome()

# Open the web application URL
driver.get("https://example.com")

# Find an input field and enter a value
input_field = driver.find_element(By.ID, "input-field")
input_field.send_keys("Hello, World!")

# Click a button
button = driver.find_element(By.ID, "submit-button")
button.click()

# Wait for a specific element to be present on the page
result_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "result"))
)

# Assert the expected result
expected_result = "Hello, World!"
actual_result = result_element.text
assert actual_result == expected_result

# Print the test result
if actual_result == expected_result:
    print("UI Test Passed!")
else:
    print("UI Test Failed!")

# Close the browser
driver.quit()


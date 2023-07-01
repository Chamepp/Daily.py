from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver (You will need to install the Selenium package and ChromeDriver)
driver = webdriver.Chrome('/path/to/chromedriver')

# Open the webpage
driver.get('https://www.example.com/form')

# Fill out the form fields
driver.find_element(By.ID, 'name').send_keys('John Doe')
driver.find_element(By.ID, 'email').send_keys('johndoe@example.com')
driver.find_element(By.ID, 'message').send_keys('Hello, this is my message!')

# Submit the form
driver.find_element(By.XPATH, '//button[contains(text(), "Submit")]').click()

# Wait for a success message or a specific element on the page after submitting the form
try:
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'success-message'))
    )
    print('Form submitted successfully!')
except:
    print('Form submission failed.')

# Close the browser
driver.quit()

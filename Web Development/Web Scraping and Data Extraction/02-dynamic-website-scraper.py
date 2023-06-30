import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver with Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
driver = webdriver.Chrome(options=chrome_options)

# URL of the dynamic website you want to scrape
url = "https://example.com"

# Open the website in the Chrome browser
driver.get(url)

# Wait for the dynamic content to load
wait = WebDriverWait(driver, 10)
dynamic_content = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "YOUR_CSS_SELECTOR")))

# Extract the desired data from the dynamic content
data = dynamic_content.text
print(data)

# Close the browser
driver.quit()


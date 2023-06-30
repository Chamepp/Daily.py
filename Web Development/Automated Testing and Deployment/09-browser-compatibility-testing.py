from selenium import webdriver

# Define the list of browsers to test
browsers = ["chrome", "firefox", "edge", "safari"]

# Specify the URL of the web application to test
url = "https://example.com"

# Loop through each browser and perform compatibility testing
for browser in browsers:
    # Initialize the WebDriver for the specified browser
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        print(f"Unsupported browser: {browser}")
        continue

    try:
        # Open the web application in the browser
        driver.get(url)
        
        # Perform browser compatibility tests
        # Add your specific test scenarios here
        
        # Example: Check if the page title is correct
        expected_title = "Example Website"
        actual_title = driver.title
        
        if expected_title == actual_title:
            print(f"[{browser}] Browser compatibility test passed.")
        else:
            print(f"[{browser}] Browser compatibility test failed.")

    finally:
        # Quit the browser after each test
        driver.quit()


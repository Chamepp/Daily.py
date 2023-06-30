from selenium import webdriver

def capture_screenshot(url, output_file):
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()

    # Navigate to the specified URL
    driver.get(url)

    # Capture a screenshot of the entire page
    driver.save_screenshot(output_file)

    # Close the browser
    driver.quit()

# Example usage
url = input("Enter the URL of the web page: ")
output_file = input("Enter the filename for the screenshot (with extension): ")

capture_screenshot(url, output_file)
print(f"Screenshot saved as {output_file}")

